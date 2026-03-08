import os
import psycopg2
from psycopg2.extras import Json
from dotenv import load_dotenv

load_dotenv()

DB = {
    "dbname": os.getenv("DB_NAME", "event_analytics"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASS", "strongpassword"),
    "host": os.getenv("DB_HOST", "localhost"),
}

def get_conn():
    return psycopg2.connect(**DB)
