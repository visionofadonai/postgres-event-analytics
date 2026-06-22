from fastapi.testclient import TestClient
from app.main import app

def test_ready_success(monkeypatch):
    class FakeConn:
        async def fetch(self, query):
            return [1]

    async def fake_init_db():
        return None

    async def fake_close_db():
        return None

    async def fake_get_conn():
        return FakeConn()

    async def fake_release_conn(conn):
        return None

    monkeypatch.setattr("app.main.init_db", fake_init_db)
    monkeypatch.setattr("app.main.close_db", fake_close_db)
    monkeypatch.setattr("app.main.get_conn", fake_get_conn)
    monkeypatch.setattr("app.main.release_conn", fake_release_conn)

    with TestClient(app) as client:
        response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready",
        "database": "reachable"
    }
