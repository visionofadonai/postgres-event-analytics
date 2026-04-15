import asyncpg
from app.config import DB_NAME, DB_USER, DB_PASS, DB_HOST

pool = None

async def init_db():
    global pool
    if pool is None:
        pool = await asyncpg.create_pool(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            min_size=1,
            max_size=10
        )

async def close_db():
    global pool
    if pool is not None:
        await pool.close()
        pool = None

async def get_conn():
    return await pool.acquire()

async def release_conn(conn):
    await pool.release(conn)
