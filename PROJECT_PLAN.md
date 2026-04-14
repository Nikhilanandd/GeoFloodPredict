# GeoFloodPredict - Structured Implementation Plan (uv + FastAPI)

## 1) Current Project Status
- `uv venv` completed
- `uv init` completed
- Project currently has basic scaffold only (`main.py`, minimal `pyproject.toml`, conceptual `README.md`)

## 2) Problem Understanding from README
GeoFloodPredict aims to predict urban flood risk by combining:
- Geospatial data (DEM, land use, drainage, etc.)
- Meteorological data (rainfall intensity/duration)
- GIS-derived features (elevation, slope, flow proxies, hydrological indicators)
- ML models to output flood risk scores/classes
- Interactive map dashboard for decision support

Pipeline target from README:
1. Data acquisition and harmonization
2. GIS feature generation
3. Feature engineering + label preparation
4. ML model training/evaluation
5. Spatial inference and risk classification
6. Dashboard visualization

## 3) Finalized Best Tech Stack

### Backend (fixed as requested)
- FastAPI
- Uvicorn (ASGI server)
- Pydantic v2 for settings and schemas
- SQLModel + Alembic for database models/migrations
- PostgreSQL + PostGIS for geospatial persistence and spatial queries
- Redis + RQ (or Celery) for background geospatial/ML jobs

### Geospatial + Data + ML
- GeoPandas, Shapely, PyProj, Rasterio, Rioxarray
- Pandas, NumPy
- Scikit-learn (baseline models)
- XGBoost (strong tabular performance for susceptibility modeling)
- Optuna (hyperparameter tuning)
- MLflow (experiment tracking and model registry)

### API + Ops + Quality
- HTTPX for external data ingestion
- Loguru or structlog for structured logging
- Pytest + pytest-asyncio for tests
- Ruff + mypy for linting/type checks
- Pre-commit hooks

### Frontend (recommended)
- React + Vite + TypeScript
- MapLibre GL JS (or Leaflet) for flood risk visualization
- Deck.gl for high-volume geospatial overlays (optional)
- Tailwind CSS for rapid UI styling

### Why this stack is best for your use case
- FastAPI gives high-performance APIs and excellent typing/docs.
- PostGIS is the most reliable spatial backend for production GIS.
- GeoPandas/Rasterio are standard for raster-vector feature engineering.
- XGBoost + scikit-learn balances model quality and maintainability.
- MLflow makes experiments reproducible and easier to promote to production.

## 4) Recommended Project Structure

```text
GeoFloodPredict/
  app/
    api/
      v1/
        routes/
    core/
      config.py
      logging.py
    db/
      models/
      session.py
      migrations/
    schemas/
    services/
      ingestion/
      geoprocessing/
      features/
      training/
      inference/
    workers/
      tasks.py
    main.py
  data/
    raw/
    interim/
    processed/
  models/
    artifacts/
  notebooks/
  tests/
    unit/
    integration/
  scripts/
  pyproject.toml
  README.md
```

## 5) Phased Delivery Plan

### Phase 0 - Foundation (Day 1-2)
- Set dependencies in `pyproject.toml` with uv
- Create FastAPI app with health endpoint
- Add environment config and logging
- Add Docker setup for PostgreSQL/PostGIS + Redis (optional but recommended)

Deliverable:
- Running API with `/health`
- DB connection verified

### Phase 1 - Data Ingestion + GIS Preprocessing (Week 1)
- Build ingestion services for DEM/rainfall/land-use/open spatial layers
- CRS harmonization and spatial extent standardization
- Generate first reusable geospatial feature set

Deliverable:
- Saved standardized dataset in `data/processed/`
- Metadata log for source, CRS, resolution, and quality checks

### Phase 2 - Feature Engineering + Labeling (Week 1-2)
- Build tabular feature matrix from GIS layers
- Handle nulls, scaling, and leakage checks
- Prepare labels from flood history/proxy definitions

Deliverable:
- Versioned training dataset
- Documented target label strategy

### Phase 3 - Model Training + Evaluation (Week 2)
- Train baseline models (LogReg/RF/XGBoost)
- Cross-validation + metric selection (ROC-AUC, PR-AUC, F1, calibration)
- Store model + feature pipeline artifacts

Deliverable:
- Best validated model
- Evaluation report + confusion matrix + feature importance

### Phase 4 - Inference + Risk Maps (Week 3)
- Batch inference across full study grid
- Convert probabilities to risk bands (low/medium/high)
- Persist geospatial outputs in PostGIS and export GeoJSON/tiles

Deliverable:
- Georeferenced risk layer ready for API serving

### Phase 5 - Dashboard + Decision Support (Week 3-4)
- Build map UI with layer toggles and zone inspection
- Add filters by ward/grid/risk class
- Add summary analytics cards

Deliverable:
- End-to-end demo: data -> model -> API -> map visualization

## 6) uv-Only Command Plan

```bash
# Already done
uv venv
uv init

# Activate env
source .venv/bin/activate

# Runtime dependencies
uv add fastapi uvicorn[standard] pydantic-settings sqlmodel alembic \
  psycopg[binary] geoalchemy2 geopandas shapely pyproj rasterio rioxarray \
  pandas numpy scikit-learn xgboost optuna mlflow httpx redis rq

# Dev dependencies
uv add --dev pytest pytest-asyncio ruff mypy pre-commit

# Run API (after app/main.py exists)
uv run uvicorn app.main:app --reload

# Run tests
uv run pytest -q

# Lint/type check
uv run ruff check .
uv run mypy app
```

## 7) Suggested Initial API Endpoints
- `GET /health`
- `POST /ingestion/jobs` to start data ingestion
- `POST /training/jobs` to start model training
- `GET /training/jobs/{job_id}` for status/metrics
- `POST /inference/jobs` to generate risk map
- `GET /risk/zones` with filters (bbox, risk_class, date)
- `GET /risk/zones/{zone_id}` detailed feature/risk explanation

## 8) Structured Prompt for an Agent
Use this prompt with a coding agent to start implementation:

```text
You are implementing GeoFloodPredict using uv as the only Python package manager.

Context:
- FastAPI backend is mandatory.
- Goal: ML-based urban flood risk prediction using geospatial + rainfall features and map-ready outputs.
- Existing repo has minimal scaffold only.

Task:
1) Create a production-ready FastAPI project structure under app/ with:
   - app/main.py
   - app/core/config.py
   - app/api/v1/routes/health.py
   - app/db/session.py
   - app/schemas/
   - app/services/
   - tests/unit/test_health.py
2) Configure pyproject.toml dependencies using uv-compatible setup.
3) Implement `/health` endpoint and basic app startup config.
4) Add placeholders/service interfaces for ingestion, feature engineering, training, and inference.
5) Add Alembic setup for SQLModel + PostgreSQL/PostGIS.
6) Add README setup steps using uv commands only.
7) Add minimal tests and ensure they pass.

Constraints:
- Use Python 3.12+
- Keep code modular and typed.
- Do not add unnecessary complexity.
- Include clear TODO markers where geospatial logic will be filled later.

Definition of done:
- `uv run uvicorn app.main:app --reload` starts successfully.
- `uv run pytest -q` passes.
- Basic linting (`ruff`) passes.
- Repo has a clean, extensible foundation for next phases.
```

## 9) Decision Notes
- Start with a strong backend and data pipeline first; dashboard can follow once inference outputs stabilize.
- Keep first model simple and explainable, then optimize.
- Prioritize reproducibility: dataset versions, model artifact versions, and tracked experiments.
