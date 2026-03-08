from fastapi import FastAPI
#from app.api import events
from app.api.events import router as events_router

app = FastAPI(title="Event Analytics API")
#app.include_router(events.router,prefix="/events")
app.include_router(events_router)
@app.get("/health")
def health():
    return {"status": "ok"}
