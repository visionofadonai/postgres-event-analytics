#!/usr/bin/env python3
import uuid, random, time
from datetime import datetime, timezone
import psycopg2
from psycopg2.extras import Json, execute_values
import os
from dotenv import load_dotenv

load_dotenv()

DB = {
    "dbname": os.getenv("DB_NAME"), 
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "host": os.getenv("DB_HOST")
}

EVENT_TYPES = ["page_view", "click", "signup", "purchase"]

def generate_event():
    return {
        "user_id": str(uuid.uuid4()),
        "event_type": random.choice(EVENT_TYPES),
        "properties": {"page": f"/product/{random.randint(1,100)}", "value": random.random()},
        "occurred_at": datetime.now(timezone.utc),
    }

def insert_batch(conn, rows):
    sql = """
    INSERT INTO events (user_id, event_type, properties, occurred_at)
    VALUES %s
    """
    vals = [(r["user_id"], r["event_type"], Json(r["properties"]), r["occurred_at"]) for r in rows]
    execute_values(conn.cursor(), sql, vals, template=None)
    conn.commit()

def main(batch_size=1000, total=10000):
    conn = psycopg2.connect(**DB)
    inserted = 0
    while inserted < total:
        batch = [generate_event() for _ in range(min(batch_size, total - inserted))]
        insert_batch(conn, batch)
        inserted += len(batch)
        print(f"Inserted {inserted}/{total}")
        time.sleep(0.1)
    conn.close()

if __name__ == "__main__":
    main(batch_size=2000, total=500000)
