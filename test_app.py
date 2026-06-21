import time

import pytest

from app import VERSION, _START_TIME, app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# /health tests


def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_content_type_is_json(client):
    response = client.get("/health")
    assert "application/json" in response.content_type


def test_health_status_is_ok(client):
    response = client.get("/health")
    data = response.get_json()
    assert data["status"] == "ok"


def test_health_version_matches(client):
    response = client.get("/health")
    data = response.get_json()
    assert data["version"] == VERSION


def test_health_uptime_is_non_negative(client):
    response = client.get("/health")
    data = response.get_json()
    assert data["uptime"] >= 0


def test_health_uptime_increases_over_time(client):
    response1 = client.get("/health")
    time.sleep(0.05)
    response2 = client.get("/health")

    uptime1 = response1.get_json()["uptime"]
    uptime2 = response2.get_json()["uptime"]

    assert uptime2 > uptime1


def test_health_uptime_reflects_start_time(client):
    """Uptime should be close to elapsed time since module was loaded."""
    before = time.monotonic() - _START_TIME
    response = client.get("/health")
    after = time.monotonic() - _START_TIME

    uptime = response.get_json()["uptime"]
    assert before <= uptime <= after


def test_health_timestamp_is_present(client):
    response = client.get("/health")
    data = response.get_json()
    assert "timestamp" in data
    assert data["timestamp"]  # non-empty


def test_health_timestamp_is_iso8601(client):
    """Timestamp should be parseable as ISO 8601 with timezone info."""
    from datetime import datetime

    response = client.get("/health")
    data = response.get_json()
    # fromisoformat handles Python's isoformat() output including +00:00
    dt = datetime.fromisoformat(data["timestamp"])
    assert dt.tzinfo is not None


def test_health_response_has_all_fields(client):
    response = client.get("/health")
    data = response.get_json()
    for field in ("status", "version", "uptime", "timestamp"):
        assert field in data, f"Missing field: {field}"
