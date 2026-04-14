"""Tests for health check endpoint."""

from fastapi.testclient import TestClient

from app.main import app


def test_health_check():
    """Test that health check endpoint returns 200 and expected schema."""
    client = TestClient(app)
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    data = response.json()

    # Verify required fields
    assert "status" in data
    assert "version" in data
    assert "timestamp" in data
    assert data["status"] == "healthy"


def test_health_check_schema():
    """Test that health response conforms to expected schema."""
    client = TestClient(app)
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    data = response.json()

    # Verify types
    assert isinstance(data["status"], str)
    assert isinstance(data["version"], str)
    assert isinstance(data["timestamp"], str)


def test_api_version():
    """Test that API version is correctly returned."""
    client = TestClient(app)
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "0.1.0"
