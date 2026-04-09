async def insert_event(conn, user_id, event_type, properties, occurred_at):
    await conn.execute("""
        INSERT INTO events (user_id, event_type, properties, occurred_at)
        VALUES ($1, $2, $3, $4)
    """, user_id, event_type, properties, occurred_at)

async def fetch_events_per_hour(conn):
    return await conn.fetch("""
        SELECT date_trunc('hour', occurred_at) AS hour,
               count(*) AS count
        FROM events
        GROUP BY hour
        ORDER BY hour;
    """)

async def fetch_events_by_type(conn):
    return await conn.fetch("""
        SELECT event_type,
               count(*) AS count
        FROM events
        GROUP BY event_type
        ORDER BY count DESC;
    """)

async def fetch_events_last_24h(conn):
    return await conn.fetchrow("""
        SELECT count(*) AS events_last_24h
        FROM events
        WHERE occurred_at > now() - interval '24 hours';
    """)

async def fetch_events_range(cur, hours):
    return await cur.fetchrow("""
        SELECT count(*)
        FROM events
        WHERE occurred_at > now() - make_interval(hours => $1)
    """, (hours))

async def get_hourly_metrics(cur):
    return await cur.fetch("""
        SELECT hour, event_count
        FROM events_hourly
        ORDER BY hour;
    """)

