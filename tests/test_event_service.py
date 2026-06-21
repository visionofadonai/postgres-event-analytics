import pytest
from app.services.event_service import events_by_type_service

class FakeConn:
    pass

@pytest.mark.asyncio
async def test_events_by_type_service(monkeypatch):
    async def fake_fetch_events_by_type(conn):
        return [
            {"event_type": "page_view", "count": 10},
            {"event_type": "click", "count": 5},
        ]

    monkeypatch.setattr(
        "app.services.event_service.fetch_events_by_type",
        fake_fetch_events_by_type,
    )

    result = await events_by_type_service(FakeConn())

    assert result == {
        "status": "success",
        "data": [
            {"event_type": "page_view", "count": 10},
            {"event_type": "click", "count": 5},
        ],
    }
