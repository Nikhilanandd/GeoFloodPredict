"""FastAPI application entry point."""

import logging

from fastapi import FastAPI
from loguru import logger

from app.api.v1.routes import get_api_router
from app.core.config import get_settings
from app.core.logging import setup_logging
from app.db.session import close_db, init_db

# Setup logging
setup_logging()

# Remove FastAPI's default logging to use loguru
for name in logging.root.manager.loggerDict:
    if name.startswith("uvicorn"):
        logging.getLogger(name).handlers = []

settings = get_settings()


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured application instance.
    """
    app = FastAPI(
        title=settings.api_title,
        version=settings.api_version,
        description=settings.api_description,
        debug=settings.debug,
    )

    # Include API router
    app.include_router(get_api_router())

    # Setup lifecycle events
    @app.on_event("startup")
    async def startup_event() -> None:
        """Initialize resources on app startup."""
        logger.info("Starting GeoFloodPredict API...")
        try:
            await init_db()
            logger.info("Database initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise

    @app.on_event("shutdown")
    async def shutdown_event() -> None:
        """Cleanup resources on app shutdown."""
        logger.info("Shutting down GeoFloodPredict API...")
        try:
            await close_db()
            logger.info("Database connection closed")
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")

    # Error handlers
    @app.exception_handler(Exception)
    async def general_exception_handler(request, exc):
        """Handle general exceptions."""
        logger.error(f"Unhandled exception: {exc}")
        return {"detail": "Internal server error"}

    return app


# Application instance
app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )
