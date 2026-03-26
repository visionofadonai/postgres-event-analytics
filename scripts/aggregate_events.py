import psycopg2
from datetime import datetime
import os
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()

connection_pool = pool.SimpleConnectionPool(
    1, 10,
    dbname = os.getenv("DB_NAME", "event_analytics"),
    user = os.getenv("DB_USER", "postgres"),
    password = os.getenv("DB_PASS", "strongpassword"),
    host = os.getenv("DB_HOST", "localhost")
)

def get_conn():
    return connection_pool.getconn()


def release_conn(conn):
    connection_pool.putconn(conn)


conn = get_conn()
cur = conn.cursor()

cur.execute("""
    INSERT INTO events_hourly (hour, event_count)
    SELECT date_trunc('hour', occurred_at) AS hour,
           count(*)
    FROM events
    GROUP BY hour
    ON CONFLICT (hour)
    DO UPDATE SET event_count = EXCLUDED.event_count;
""")

conn.commit()

cur.close()
release_conn(conn)

print("Aggregation complete at", datetime.now())
