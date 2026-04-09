def fetch_events_per_hour(cur):
    return cur.fetch("""
        SELECT date_trunc('hour', occurred_at), count(*)
        FROM events
        GROUP BY 1
        ORDER BY 1;
    """)

def fetch_events_by_type(cur):
    return cur.fetch("""
        SELECT event_type, count(*)
        FROM events
        GROUP BY event_type
        ORDER BY count DESC;
    """)

def fetch_events_last_24h(cur):
    return cur.fetch("""
        SELECT count(*)
        FROM events
        WHERE occurred_at > now() - interval '24 hours'
    """)

def fetch_events_range(cur, hours):
    return cur.fetchrow("""
        SELECT count(*)
        FROM events
        WHERE occurred_at > now() - make_interval(hours => $1)
    """, (hours))

def get_hourly_metrics(cur):
    return cur.fetch("""
        SELECT hour, event_count
        FROM events_hourly
        ORDER BY hour;
    """) 
