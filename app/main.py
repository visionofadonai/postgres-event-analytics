import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.extension import _rate_limit_exceeded_handler

from app.async_db import init_db, close_db
from app.middleware import log_requests
from app.api.v1.events import router as events_router
from app.api.v1.tickets import router as tickets_router
from app.config import APP_TITLE
from app.limiter import limiter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application and initializing database pool")
    await init_db()
    yield
    logger.info("Shutting down application and closing database pool")
    await close_db()

app = FastAPI(
    title="TicketFlow Backend Service",
    description="Backend analytics service built with FastAPI and PostgreSQL",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.include_router(events_router, prefix="/api/v1")
app.include_router(tickets_router, prefix="/api/v1")

app.middleware("http")(log_requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://llp"],  # replace with your real allowed origin
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

@app.get("/health")
async def health():
    return {"status": "ok"}
