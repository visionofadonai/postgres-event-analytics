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
