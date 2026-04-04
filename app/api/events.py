from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from app.db import get_conn, release_conn
from psycopg2.extras import Json
from app.queries import *
from app.async_db import get_conn, release_conn

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
async def events_per_hour():
    conn = await get_conn()
    # cur = conn.cursor()

    try:
        rows = fetch_events_per_hour(conn)
    finally:
        # cur.close()
        release_conn(conn)

    return [
        {"hour": str(r[0]), "count": r[1]}
        for r in rows
    ]

@router.get("/metrics/events-by-type")
def events_by_type():
    conn = get_conn()
    cur = conn.cursor()
    
    try:
        rows = fetch_events_by_type(cur)
    finally:
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

    try:
        count = fetch_events_last_24h(cur)
    finally:
        cur.close()
        release_conn(conn)

    return {"events_last_24h": count}

@router.get("/metrics/events-range")
def events_range(hours: int = 24):
    conn = get_conn()
    cur = conn.cursor()

    try:
        count = fetch_events_range(cur,hours)
    finally:
        cur.close()
        release_conn(conn)

    return {"count": count}

@router.get("/metrics/hourly-metrics")
def hourly_metrics():
    conn = get_conn()
    cur = conn.cursor()

    try: 
        rows = get_hourly_metrics(cur)
    finally:
        cur.close()
        release_conn(conn)

    return [
            {"hour": r[0], "count": r[1]}
            for r in rows
    ] 
