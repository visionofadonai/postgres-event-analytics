import logging
from fastapi import FastAPI, Request
from app.api import events, tickets
from app.async_db import init_db, close_db, get_conn, release_conn
from app.config import APP_TITLE, LOG_LEVEL
from app.middleware import log_requests
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.extension import _rate_limit_exceeded_handler
from .limiter import limiter


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PostgreSQL Event Analytics Service",
    description="Backend analytics service build with FastAPI and PostgreSQL",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(tickets.router)


app.include_router(events.router)
app.middleware("http")(log_requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://llp"], 
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

@app.on_event("startup")
async def startup():
    logger.info("Starting application and initializing database pool")
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    logger.info("Shutting doen application and closing database pool")
    await close_db()

@app.get("/health")
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

@app.get("/test")
@limiter.limit("10/minute")
async def test_route(request: Request):
    return {"message": "Success"}
