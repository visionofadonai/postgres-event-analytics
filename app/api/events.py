from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from app.db import get_conn
from psycopg2.extras import Json

router = APIRouter()

class EventIn(BaseModel):
    user_id: str
    event_type: str
    properties: dict
    occurred_at: datetime | None = None

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
        conn.close()
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
    conn.close()

    return [
        {"hour": str(r[0]), "count": r[1]}
        for r in rows
    ]
