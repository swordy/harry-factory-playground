import json
import pytest
from app import app, VERSION


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_version_status(client):
    response = client.get("/version")
    assert response.status_code == 200


def test_get_version_body(client):
    response = client.get("/version")
    data = json.loads(response.data)
    assert data == {"version": VERSION}


def test_get_version_content_type(client):
    response = client.get("/version")
    assert response.content_type == "application/json"
