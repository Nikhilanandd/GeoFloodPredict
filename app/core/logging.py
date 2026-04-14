"""Logging configuration."""

import sys

from loguru import logger

from app.core.config import get_settings


def setup_logging() -> None:
    """Configure structured logging with loguru."""
    settings = get_settings()

    # Remove default handler
    logger.remove()

    # Add console handler with format
    logger.add(
        sys.stderr,
        format=(
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
        level=settings.log_level,
    )

    # TODO: Add file handler for production deployments
    # logger.add("logs/app.log", rotation="500 MB", retention="7 days")
