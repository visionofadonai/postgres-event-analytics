import os
import psycopg2
from dotenv import load_dotenv


def get_conn():
    load_dotenv()
    return psycopg2.connect(
        dbname = os.getenv("DB_NAME", "event_analytics"),
        user = os.getenv("DB_USER", "postgres"),
        password = os.getenv("DB_PASS", "strongpassword"),
        host = os.getenv("DB_HOST", "localhost")
    )
