import logging
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
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
from app.api.v1.events import router as events_router
from app.api.v1.tickets import router as tickets_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs ON STARTUP
    logger.info("Starting application and initializing database pool")
    await init_db()
    
    yield  # The application serves requests while paused here
    
    # This runs ON SHUTDOWN
    logger.info("Shutting doen application and closing database pool")
    await close_db()



app = FastAPI(title="TicketFlow Backend Service",lifespan=lifespan)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="TicketFlow Backend Service",
    description="Backend analytics service build with FastAPI and PostgreSQL",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(events_router, prefix="/api/v1")
app.include_router(tickets_router, prefix="/api/v1")

app.middleware("http")(log_requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://llp"], #Update to production domain upon release 
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

@app.get("/test")
@limiter.limit("10/minute")
async def test_route(request: Request):
    return {"message": "Success"}

@app.get("/health")
async def health():
    return {"status": "ok"}

