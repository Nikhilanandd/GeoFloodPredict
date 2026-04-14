"""Application configuration management."""

from functools import lru_cache

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # API
    api_title: str = "GeoFloodPredict"
    api_version: str = "0.1.0"
    api_description: str = "ML-based urban flood risk prediction system"
    debug: bool = False

    # Database
    database_url: str = "postgresql://user:password@localhost/geofloodpredict"
    database_echo: bool = False

    # Redis
    redis_url: str = "redis://localhost:6379"

    # MLflow
    mlflow_tracking_uri: str = "http://localhost:5000"
    mlflow_experiment_name: str = "geofloodpredict"

    # Logging
    log_level: str = "INFO"

    # Data paths
    data_dir: str = "data"
    models_dir: str = "models"

    model_config = ConfigDict(env_file=".env", case_sensitive=False)


@lru_cache
def get_settings() -> Settings:
    """Get application settings (cached)."""
    return Settings()
