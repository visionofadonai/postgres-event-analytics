import logging
from fastapi import FastAPI
from app.api import events
from app.async_db import init_db, close_db
from app.config import APP_TITLE, LOG_LEVEL
from app.middleware import log_requests
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PostgreSQL Event Analytics Service",
    description="Backend analytics service build with FastAPI and PostgreSQL",
    version="1.0.0",
    docs_uri="/docs",
    redoc_url="/redoc",
)
app.include_router(events.router)
app.middleware("http")(log_requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    logger.info("Starting application and initializing database pool")
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    logger.info("Shutting doen application and closing database pool")
    await close_db()

@app.get("/health")
def health():
    return {"status": "ok"}

