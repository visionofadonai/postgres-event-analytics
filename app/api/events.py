import logging
from fastapi import APIRouter, HTTPException
from app.async_db import get_conn, release_conn
from app.schemas.event_schema import EventIn
from app.services.event_service import (
    create_event_service,
    events_per_hour_service,
    events_by_type_service,
    events_last_24h_service,
)

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/events")
async def create_event(payload: EventIn):
    logger.info("Received event insert request for event_type=%s", payload.event_type)
    conn = await get_conn()
    try:
        return await create_event_service(conn, payload)
    except Exception as e:
        logger.exception("Failed to create event")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await release_conn(conn)

@router.get("/metrics/events-per-hour")
async def events_per_hour():
    conn = await get_conn()
    try:
        return await events_per_hour_service(conn)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await release_conn(conn)

@router.get("/metrics/events-by-type")
async def events_by_type():
    conn = await get_conn()
    try:
        return await events_by_type_service(conn)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await release_conn(conn)

@router.get("/metrics/events-last-24h")
async def events_last_24h():
    conn = await get_conn()
    try:
        return await events_last_24h_service(conn)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await release_conn(conn)
