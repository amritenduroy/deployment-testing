import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_hello_response_body(client):
    response = client.get("/")
    data = response.get_json()
    assert data["message"] == "Hello, World Butu Mum!"


def test_hello_content_type(client):
    response = client.get("/")
    assert response.content_type == "application/json"


def test_health_status_code(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_response_body(client):
    response = client.get("/health")
    data = response.get_json()
    assert data["status"] == "healthy"


def test_not_found(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
