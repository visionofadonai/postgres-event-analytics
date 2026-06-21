from fastapi import APIRouter
from app.async_db import init_db, close_db, get_conn, release_conn

router = APIRouter(tags=["health"])

@router.get("/health")
async def health():
    conn = await get_conn()

    try:
        await conn.fetch("SELECT 1")
    finally:
        await release_conn(conn)

    return {
        "status": "ok",
        "database": "reachable"
    }

