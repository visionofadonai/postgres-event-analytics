from datetime import datetime
from typing import Any
from pydantic import BaseModel

class EventIn(BaseModel):
    user_id: str
    event_type: str
    properties: dict[str, Any]
    occurred_at: datetime | None = None

class EventCreateResponse(BaseModel):
    status: str

class EventPerHourOut(BaseModel):
    hour: str
    count: int

class EventByTypeOut(BaseModel):
    event_type: str
    count: int

class EventLast24hOut(BaseModel):
    events_last_24h: int
