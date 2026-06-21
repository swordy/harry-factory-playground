"""Tests for the /health endpoint."""

import time
from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient

from app.main import app, _START_TIME, APP_VERSION

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for GET /health."""

    def test_returns_200(self):
        """R1: GET /health must return HTTP 200."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_content_type_is_json(self):
        """Response Content-Type should be application/json."""
        response = client.get("/health")
        assert "application/json" in response.headers["content-type"]

    def test_body_contains_status(self):
        """R2: Body must expose 'status' field."""
        response = client.get("/health")
        body = response.json()
        assert "status" in body
        assert body["status"] in ("ok", "degraded")

    def test_body_contains_version(self):
        """R2: Body must expose 'version' field."""
        response = client.get("/health")
        body = response.json()
        assert "version" in body
        assert isinstance(body["version"], str)
        assert body["version"] != ""

    def test_version_matches_app_version(self):
        """Version in response matches APP_VERSION constant."""
        response = client.get("/health")
        body = response.json()
        assert body["version"] == APP_VERSION

    def test_body_contains_uptime(self):
        """R2: Body must expose 'uptime' field."""
        response = client.get("/health")
        body = response.json()
        assert "uptime" in body
        assert isinstance(body["uptime"], (int, float))
        assert body["uptime"] >= 0

    def test_uptime_is_non_negative_at_fresh_startup(self):
        """Uptime should be >= 0 even immediately after startup."""
        response = client.get("/health")
        body = response.json()
        assert body["uptime"] >= 0

    def test_uptime_increments_over_time(self):
        """Uptime should increase between successive calls."""
        first = client.get("/health").json()["uptime"]
        time.sleep(0.05)
        second = client.get("/health").json()["uptime"]
        assert second > first

    def test_body_contains_timestamp(self):
        """Response body should include a timestamp field."""
        response = client.get("/health")
        body = response.json()
        assert "timestamp" in body
        # Must be parseable as ISO 8601
        ts = datetime.fromisoformat(body["timestamp"])
        # Must be timezone-aware
        assert ts.tzinfo is not None

    def test_timestamp_is_recent(self):
        """Timestamp in response should be close to now."""
        before = datetime.now(timezone.utc)
        response = client.get("/health")
        after = datetime.now(timezone.utc)
        ts = datetime.fromisoformat(response.json()["timestamp"])
        assert before <= ts <= after

    def test_cache_control_header_set(self):
        """Cache-Control header should prevent stale health data."""
        response = client.get("/health")
        assert "cache-control" in response.headers
        assert "no-store" in response.headers["cache-control"]

    def test_idempotent_multiple_calls(self):
        """Multiple calls should all return 200 with consistent shape."""
        for _ in range(5):
            response = client.get("/health")
            assert response.status_code == 200
            body = response.json()
            assert "status" in body
            assert "version" in body
            assert "uptime" in body
            assert "timestamp" in body
