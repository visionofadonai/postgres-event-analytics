import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("DB_PASSWORD")

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST")
)

cur = conn.cursor()

cur.execute("SELECT version();")

print(cur.fetchone())

cur.close()
conn.close()
