#import sys
#import os
#print("Python Executable:", sys.executable)
#print("Current Working Directory:", os.getcwd())
#print("Python Path:", sys.path)
from fastapi import FastAPI
from app.api import events
from app.async_db import init_db


app = FastAPI(title="Event Analytics API")
app.include_router(events.router)
@app.get("/health")
def health():
    return {"status": "ok"}

@app.on_event("startup")
async def startup():
    await init_db()
