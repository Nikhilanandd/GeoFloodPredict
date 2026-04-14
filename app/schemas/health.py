"""Health check schemas."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    version: str
    timestamp: datetime
    database: str | None = None
    redis: str | None = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "healthy",
                "version": "0.1.0",
                "timestamp": "2024-01-01T12:00:00Z",
                "database": "connected",
                "redis": "connected",
            }
        }
    )
