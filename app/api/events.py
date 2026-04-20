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
    logger.info(
        "create_event_request", 
        extra = {"event_type":payload.event_type}
    )
    conn = await get_conn()
    try:
        return await create_event_service(conn, payload)
    except Exception as e:
        logger.exception("create_event_failed")
        raise HTTPException(
            status_code=500, 
            detail="Internal server error"
        )
    finally:
        await release_conn(conn)

@router.get("/metrics/events-per-hour")
async def events_per_hour():
    logger.info(
        "events_per_hour_request"
    )
    conn = await get_conn()
    try:
        return await events_per_hour_service(conn)
    except Exception as e:
        logger.exception("events_per_hour_failed")
        raise HTTPException(
            status_code=500, 
            detail="Internal server error"
        )
    finally:
        await release_conn(conn)

@router.get("/metrics/events-by-type")
async def events_by_type():
    logger.info(
        "events_by_type_request"
    )
    conn = await get_conn()
    try:
        return await events_by_type_service(conn)
    except Exception as e:
        logger.exception("events_by_type_service_failed")
        raise HTTPException(
            status_code=500, 
            detail="Internal server error"
        )
    finally:
        await release_conn(conn)

@router.get("/metrics/events-last-24h")
async def events_last_24h():
    logger.info(
        "events_last_24h_request"
    )
    conn = await get_conn()
    try:
        return await events_last_24h_service(conn)
    except Exception as e:
        logger.exception("events_last_24h_failed")
        raise HTTPException(
            status_code=500, 
            detail="Internal server error"
        )
    finally:
        await release_conn(conn)
