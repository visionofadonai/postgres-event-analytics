from datetime import datetime, timezone
from app.repositories.event_repository import *

async def create_event_service(conn, payload):
    occurred_at = payload.occurred_at or datetime.now(timezone.utc)
    await insert_event(
        conn,
        payload.user_id,
        payload.event_type,
        payload.properties,
        occurred_at,
    )
    return {"status": "ok"}

async def events_per_hour_service(conn):
    rows = await fetch_events_per_hour(conn)
    return [{"hour": str(r["hour"]), "count": r["count"]} for r in rows]

async def events_by_type_service(conn):
    rows = await fetch_events_by_type(conn)
    return [{"event_type": r["event_type"], "count": r["count"]} for r in rows]

async def events_last_24h_service(conn):
    row = await fetch_events_last_24h(conn)
    return {"events_last_24h": row["events_last_24h"]}
