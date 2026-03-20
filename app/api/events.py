from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from app.db import get_conn, release_conn
from psycopg2.extras import Json

router = APIRouter()

class EventIn(BaseModel):
    user_id: str
    event_type: str
    properties: dict
    occurred_at: datetime | None = None

@router.get("/events/")
async def read_events():
    return [{"event_id": "1"}, {"event_id": "2"}]

@router.post("/events")
def create_event(payload: EventIn):
    conn = get_conn()
    cur = conn.cursor()
    occurred_at = payload.occurred_at or datetime.utcnow()
    try:
        cur.execute(
            "INSERT INTO events (user_id, event_type, properties, occurred_at) VALUES (%s,%s,%s,%s)",
            (payload.user_id, payload.event_type, Json(payload.properties), occurred_at)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        release_conn(conn)
    return {"status": "ok"}

@router.get("/metrics/events-per-hour")
def events_per_hour():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT date_trunc('hour', occurred_at) AS hour,
               count(*)
        FROM events
        GROUP BY hour
        ORDER BY hour;
    """)

    rows = cur.fetchall()

    cur.close()
    release_conn(conn)

    return [
        {"hour": str(r[0]), "count": r[1]}
        for r in rows
    ]

@router.get("/metrics/events-by-type")
def events_by_type():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT event_type, count(*)
        FROM events
        GROUP BY event_type
        ORDER BY count DESC;
    """)

    rows = cur.fetchall()

    cur.close()
    release_conn(conn)

    return [
        {"event_type": r[0], "count": r[1]}
        for r in rows
    ]

@router.get("/metrics/events-last-24h")
def events_last_24h():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT count(*)
        FROM events
        WHERE occurred_at > now() - interval '24 hours'
    """)

    count = cur.fetchone()[0]

    cur.close()
    release_conn(conn)

    return {"events_last_24h": count}
