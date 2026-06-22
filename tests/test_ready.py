from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ready(monkeypatch):

    class FakeConn:
        async def fetch(self, query):
            return [1]

    async def fake_get_conn():
        return FakeConn()

    async def fake_release_conn(conn):
        pass

    monkeypatch.setattr(
        "app.main.get_conn",
        fake_get_conn
    )

    monkeypatch.setattr(
        "app.main.release_conn",
        fake_release_conn
    )

    response = client.get("/ready")

    assert response.status_code == 200

    assert response.json() == {
        "status": "ready",
        "database": "reachable"
    }
