def fetch_events_per_hour(cur):
    cur.execute("""
        SELECT date_trunc('hour', occurred_at), count(*)
        FROM events
        GROUP BY 1
        ORDER BY 1;
    """)
    return cur.fetchall()


def fetch_events_by_type(cur):
    cur.execute("""
        SELECT event_type, count(*)
        FROM events
        GROUP BY event_type
        ORDER BY count DESC;
    """)
    return cur.fetchall()

def fetch_events_last_24h(cur):
    cur.execute("""
        SELECT count(*)
        FROM events
        WHERE occurred_at > now() - interval '24 hours'
    """)
    return cur.fetchone()[0]

def fetch_events_range(cur, hours):
    cur.execute("""
        SELECT count(*)
        FROM events
        WHERE occurred_at > now() - make_interval(hours => %s)
    """, (hours,))


    return cur.fetchone()[0]

def get_hourly_metrics(cur):
    cur.execute("""
        SELECT hour, event_count
        FROM events_hourly
        ORDER BY hour;
    """)
    return cur.fetchall()
