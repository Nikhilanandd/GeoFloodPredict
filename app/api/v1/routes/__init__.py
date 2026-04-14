"""API v1 routes."""

from fastapi import APIRouter

from app.api.v1.routes.health import router as health_router


def get_api_router() -> APIRouter:
    """Create and return the main API router with all route modules."""
    router = APIRouter(prefix="/api/v1")
    router.include_router(health_router, tags=["health"])

    # TODO: Add more route modules here as they are developed
    # router.include_router(ingestion_router, tags=["ingestion"])
    # router.include_router(training_router, tags=["training"])
    # router.include_router(inference_router, tags=["inference"])
    # router.include_router(risk_router, tags=["risk"])

    return router
