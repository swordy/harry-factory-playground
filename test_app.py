import pytest
from app import app, VERSION, STATUS


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# /status tests

def test_get_status_returns_200(client):
    response = client.get("/status")
    assert response.status_code == 200


def test_get_status_content_type_is_html(client):
    response = client.get("/status")
    assert "text/html" in response.content_type


def test_get_status_body_contains_version(client):
    response = client.get("/status")
    assert VERSION.encode() in response.data


def test_get_status_body_contains_state(client):
    response = client.get("/status")
    assert STATUS.encode() in response.data
