"""Tests for the /version endpoint.

Covers:
  R1 — GET /version returns HTTP 200
  R2 — response body contains the git short sha
"""

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
def test_get_version_returns_200(client):
    response = client.get("/version")
    assert response.status_code == 200


# R2
def test_get_version_body_contains_sha(client):
    response = client.get("/version")
    data = response.json()
    assert data["sha"] == _TEST_SHA
