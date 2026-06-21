"""Tests for the /health endpoint.

Covers:
  R1 — GET /health returns HTTP 200
  R2 — response body contains the application version (git short sha)
  R3 — response body contains uptime_seconds as a non-negative number
  R4 — uptime_seconds is accurate (grows with elapsed time)
  R5 — response body contains status field equal to "ok"
"""

import time

import pytest
from starlette.testclient import TestClient

from app.main import create_app

_TEST_SHA = "abc1234"


@pytest.fixture()
def client():
    app = create_app(sha=_TEST_SHA)
    with TestClient(app) as c:
        yield c


# R1
def test_get_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


# R2
def test_get_health_body_contains_version(client):
    response = client.get("/health")
    data = response.json()
    assert data["version"] == _TEST_SHA


# R3
def test_get_health_body_contains_uptime_seconds(client):
    response = client.get("/health")
    data = response.json()
    assert "uptime_seconds" in data
    assert isinstance(data["uptime_seconds"], (int, float))
    assert data["uptime_seconds"] >= 0


# R4
def test_get_health_uptime_increases_over_time():
    """Uptime must grow between successive calls from the same app instance."""
    app = create_app(sha=_TEST_SHA)
    with TestClient(app) as c:
        first = c.get("/health").json()["uptime_seconds"]
        time.sleep(0.05)
        second = c.get("/health").json()["uptime_seconds"]
    assert second > first


# R5
def test_get_health_body_contains_status_ok(client):
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "ok"


# R6 — uptime resets when a new app instance is created
def test_get_health_uptime_resets_on_new_app_instance():
    """Each create_app() call starts a fresh uptime counter."""
    # Run first app long enough to accumulate uptime
    app_a = create_app(sha=_TEST_SHA)
    with TestClient(app_a) as c:
        time.sleep(0.05)
        uptime_a = c.get("/health").json()["uptime_seconds"]

    # Second app starts fresh — its uptime must be less than app_a's
    app_b = create_app(sha=_TEST_SHA)
    with TestClient(app_b) as c:
        uptime_b = c.get("/health").json()["uptime_seconds"]

    assert uptime_b < uptime_a
