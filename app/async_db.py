import asyncpg
import os

pool = None

async def init_db():
    global pool
    pool = await asyncpg.create_pool(
        database=os.getenv("DB_NAME", "event_analytics"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASS", ""),
        host=os.getenv("DB_HOST", "localhost"),
        min_size=1,
        max_size=10
    )

async def get_conn():
    return await pool.acquire()

async def release_conn(conn):
    await pool.release(conn)
