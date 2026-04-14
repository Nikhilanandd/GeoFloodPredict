"""Health check endpoint."""

from datetime import UTC, datetime

from fastapi import APIRouter

from app.core.config import get_settings
from app.schemas.health import HealthResponse

router = APIRouter()
settings = get_settings()


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Health check endpoint.

    Returns the application status, version, and connectivity info.
    """
    return HealthResponse(
        status="healthy",
        version=settings.api_version,
        timestamp=datetime.now(UTC),
        database="pending",  # TODO: Check database connection
        redis="pending",  # TODO: Check Redis connection
    )
