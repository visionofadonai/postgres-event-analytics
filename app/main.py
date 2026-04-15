import logging
from fastapi import FastAPI
from app.api import events
from app.async_db import init_db, close_db
from app.config import APP_TITLE, LOG_LEVEL

logging.basicConfig(level=getattr(logging, LOG_LEVEL.upper(), logging.INFO))
logger = logging.getLogger(__name__)

app = FastAPI(title=APP_TITLE)
app.include_router(events.router)

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

