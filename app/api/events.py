from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from app.db import get_conn, release_conn
from psycopg2.extras import Json
from app.queries import *
from app.async_db import get_conn, release_conn
from app.schemas.event_schema import *

router = APIRouter()

@router.get("/events/")
async def read_events():
    return [{"event_id": "1"}, {"event_id": "2"}]


@router.post("/events")
async def create_event(payload: EventIn):
    conn = await get_conn()
    occurred_at = payload.occurred_at or datetime.utcnow()
    
    try:
        await cur.execute(
            "INSERT INTO events (user_id, event_type, properties, occurred_at) VALUES (%s,%s,%s,%s)",
            (payload.user_id, payload.event_type, Json(payload.properties), occurred_at)
        )
        await conn.commit()
    except Exception as e:
        await conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await release_conn(conn)
    return {"status": "ok"}

@router.get("/metrics/events-per-hour")
async def events_per_hour():
    conn = await get_conn()
    try:
        rows = await fetch_events_per_hour(conn)
    finally:
        await release_conn(conn)

    return [
        {"hour": str(r[0]), "count": r[1]}
        for r in rows
    ]

@router.get("/metrics/events-by-type")
async def events_by_type():
    conn = await get_conn()
    
    try:
        rows = await fetch_events_by_type(conn)
    finally:
        await release_conn(conn)

    return [
        {"event_type": r[0], "count": r[1]}
        for r in rows
    ]

@router.get("/metrics/events-last-24h")
async def events_last_24h():
    conn = await get_conn()

    try:
        count = await fetch_events_last_24h(conn)
    finally:
        await release_conn(conn)

    return {"events_last_24h": count}

@router.get("/metrics/events-range")
async def events_range(hours: int = 24):
    conn = await get_conn()

    try:
        count = await fetch_events_range(conn,hours)
    finally:
        await release_conn(conn)

    return {"count": count}

@router.get("/metrics/hourly-metrics")
async def hourly_metrics():
    conn = await get_conn()

    try: 
        rows = await fetch_events_per_hour(conn)

    finally:
        release_conn(conn)

    return [
            {"hour": r[0], "count": r[1]}
            for r in rows
    ] 
