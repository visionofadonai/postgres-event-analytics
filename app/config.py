import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", "event_analytics")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "")
DB_HOST = os.getenv("DB_HOST", "localhost")

APP_TITLE = os.getenv("APP_TITLE", "Event Analytics API")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
