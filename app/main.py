from fastapi import FastAPI
from app.api import events
from app.async_db import init_db, close_db


app = FastAPI(title="PostgreSQL Event Analytics Service")

@app.on_event("startup")
async def startup():
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()

app.include_router(events.router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.on_event("startup")
async def startup():
    await init_db()
