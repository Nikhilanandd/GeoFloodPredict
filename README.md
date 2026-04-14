# GeoFloodPredict - ML-Based Urban Flood Risk Prediction System

A machine learning-based flood risk prediction system that utilizes open geospatial and meteorological data to identify urban flood-prone zones.

By integrating GIS processing, digital elevation models, rainfall data, and feature engineering techniques, the project aims to develop a cost-effective and scalable predictive framework. The system supports spatial visualization through an interactive dashboard to assist urban planners and disaster management authorities in data-driven decision-making.

---

## 🎯 Project Goals

- Identify flood-prone urban zones using open-source datasets
- Build reliable flood susceptibility models from GIS-derived features
- Enable early risk understanding for planning and mitigation
- Provide interpretable spatial outputs for policy and operations
- Develop a scalable and cost-effective framework for different cities

---

## ✨ Key Features

- **Open geospatial data integration** (DEM, land use, drainage, rainfall, etc.)
- **GIS-based preprocessing** for terrain and hydrological feature extraction
- **Machine learning flood risk modeling** with engineered environmental features
- **Urban flood zone classification** into risk categories
- **Interactive spatial dashboard** for map-based risk visualization
- **Scalable architecture** for adaptation to multiple urban regions
- **Production-ready FastAPI backend** with async support
- **PostgreSQL + PostGIS** for spatial data persistence
- **Experiment tracking** with MLflow

---

## 🏗️ Architecture

### Technology Stack

**Backend:**
- FastAPI (web framework)
- Uvicorn (ASGI server)
- SQLModel + Alembic (ORM & migrations)
- PostgreSQL + PostGIS (geospatial database)
- Redis + RQ (async task queue)

**Geospatial & ML:**
- GeoPandas, Shapely, PyProj (geospatial libraries)
- Rasterio, Rioxarray (raster processing)
- Scikit-learn, XGBoost (modeling)
- Optuna (hyperparameter tuning)
- MLflow (experiment tracking)

**Quality & Testing:**
- Pytest, pytest-asyncio (testing)
- Ruff (linting)
- Mypy (type checking)
- Pre-commit hooks

**Frontend (Future Phase):**
- React + Vite + TypeScript
- MapLibre GL JS for spatial visualization
- Tailwind CSS

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- `uv` package manager (https://github.com/astral-sh/uv)
- PostgreSQL with PostGIS (optional for dev, required for production)
- Redis (optional for dev, required for background jobs)

### Installation

1. **Clone the repository:**
   ```bash
   cd GeoFloodPredict
   ```

2. **Create and activate a virtual environment:**
   ```bash
   source .venv/bin/activate
   ```
   *(Already created via `uv venv` — if not, run `uv venv`)*

3. **Install dependencies:**
   ```bash
   # Runtime dependencies (already installed)
   uv add fastapi uvicorn[standard] pydantic-settings sqlmodel alembic \
     psycopg[binary] asyncpg geoalchemy2 geopandas shapely pyproj rasterio \
     rioxarray pandas numpy scikit-learn xgboost optuna mlflow httpx redis \
     rq python-dotenv loguru

   # Development dependencies (already installed)
   uv add --dev pytest pytest-asyncio pytest-cov ruff mypy types-redis pre-commit
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your database and service settings
   ```

5. **Verify setup:**
   ```bash
   # Run tests
   uv run pytest tests/ -q

   # Check linting
   uv run ruff check .
   ```

6. **Start the API server (requires PostgreSQL running):**
   ```bash
   uv run uvicorn app.main:app --reload
   ```

   The API will be available at: `http://localhost:8000`
   - API docs (Swagger UI): `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`
   - OpenAPI schema: `http://localhost:8000/openapi.json`

---

## 📋 Development Commands

### Running the Application

```bash
# Activate venv (if not already active)
source .venv/bin/activate

# Run development server (with hot reload)
uv run uvicorn app.main:app --reload

# Run production server
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Testing

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/unit/test_health.py -v

# Run with coverage report
uv run pytest --cov=app --cov-report=html

# Run tests in watch mode
uv run ptw
```

### Code Quality

```bash
# Lint code
uv run ruff check .

# Auto-fix linting issues
uv run ruff check . --fix

# Type checking
uv run mypy app

# Run pre-commit checks (all files)
uv run pre-commit run --all-files
```

---

## 📂 Project Structure

```
GeoFloodPredict/
├── app/                          # Main application package
│   ├── api/                      # API routes
│   │   └── v1/
│   │       └── routes/
│   │           └── health.py     # ✅ Health check endpoint
│   ├── core/
│   │   ├── config.py            # ✅ App settings from environment
│   │   ├── logging.py           # ✅ Logging configuration
│   │   └── __init__.py
│   ├── db/
│   │   ├── session.py           # ✅ Database session & engine
│   │   ├── models/              # Database ORM models (TODO)
│   │   └── __init__.py
│   ├── schemas/                 # Pydantic request/response schemas
│   │   ├── health.py            # ✅ Health response schema
│   │   └── __init__.py
│   ├── services/                # Business logic services
│   │   ├── ingestion/           # Data ingestion (TODO: Phase 1)
│   │   ├── geoprocessing/       # GIS operations (TODO: Phase 1)
│   │   ├── features/            # Feature engineering (TODO: Phase 2)
│   │   ├── training/            # Model training (TODO: Phase 3)
│   │   ├── inference/           # Model inference (TODO: Phase 4)
│   │   └── __init__.py
│   ├── workers/                 # Background job workers
│   │   ├── tasks.py             # RQ/Celery task definitions (TODO)
│   │   └── __init__.py
│   ├── main.py                  # ✅ FastAPI app factory
│   └── __init__.py
├── tests/                        # Test suite
│   ├── unit/
│   │   ├── test_health.py       # ✅ Health endpoint tests
│   │   └── __init__.py
│   ├── integration/             # Integration tests (TODO)
│   │   └── __init__.py
│   └── conftest.py              # ✅ Pytest fixtures
├── data/                        # Data directories (git-ignored content)
│   ├── raw/                     # Original datasets
│   ├── interim/                 # Intermediate processing
│   └── processed/               # Final datasets
├── models/
│   └── artifacts/               # Trained model files
├── notebooks/                   # Jupyter notebooks (TODO)
├── scripts/                     # Utility scripts (TODO)
├── pyproject.toml              # ✅ Project metadata & dependencies
├── .env.example                # ✅ Environment variables template
├── .gitignore                  # ✅ Git ignore rules
├── .pre-commit-config.yaml     # ✅ Pre-commit hooks config
├── PROJECT_PLAN.md             # Detailed implementation roadmap
└── README.md                   # This file
```

---

## 🔄 Development Phases

### Phase 0: Foundation ✅ **COMPLETE**
- [x] FastAPI project scaffold
- [x] Basic configuration and logging
- [x] Health check endpoint with tests
- [x] Database session setup (SQLModel + Alembic)
- [x] Async PostgreSQL support
- [x] Test suite and linting passing
- [x] Python 3.12+ support

**Current Status:** API starts, tests pass, linting clean. Ready for Phase 1.

### Phase 1: Data Ingestion + GIS Preprocessing (Next)
- [ ] DEM data download and harmonization
- [ ] Rainfall data collection
- [ ] Land use layer integration
- [ ] CRS standardization and spatial extent alignment
- [ ] Ingestion service endpoints

### Phase 2: Feature Engineering + Labeling
- [ ] Tabular feature matrix construction
- [ ] Terrain-derived features (slope, aspect, TPI)
- [ ] Hydrological indicators (flow accumulation, wetness)
- [ ] Meteorological feature aggregation
- [ ] Feature normalization and encoding

### Phase 3: Model Training + Evaluation
- [ ] Baseline model training (LogisticRegression, RandomForest, XGBoost)
- [ ] Cross-validation and hyperparameter optimization
- [ ] Model evaluation (ROC-AUC, PR-AUC, calibration curves)
- [ ] Model artifact persistence and versioning

### Phase 4: Inference + Risk Maps
- [ ] Batch inference on full urban grid
- [ ] Risk score → risk class conversion
- [ ] GeoJSON/GeoTIFF output generation
- [ ] PostGIS risk layer persistence

### Phase 5: Dashboard + Decision Support
- [ ] React + MapLibre GL JS interactive map
- [ ] Layer toggling and spatial filtering
- [ ] Risk zone details and explanations
- [ ] Summary analytics cards
- [ ] End-to-end data flow demonstration

---

## 🔌 API Endpoints (Planned)

```
GET  /health                              # Application health
GET  /docs                               # OpenAPI/Swagger UI
GET  /openapi.json                       # OpenAPI schema

POST /api/v1/ingestion/jobs              # Start data ingestion (Phase 1)
POST /api/v1/training/jobs               # Start model training (Phase 3)
GET  /api/v1/training/jobs/{job_id}     # Training job status (Phase 3)
POST /api/v1/inference/jobs              # Generate risk map (Phase 4)
GET  /api/v1/risk/zones                  # List risk zones with filters (Phase 4)
GET  /api/v1/risk/zones/{zone_id}       # Risk zone spatial details (Phase 4)
```

---

## 🗄️ Database Setup

### PostgreSQL + PostGIS

Required for full functionality:

```bash
# Create database with PostGIS
createdb geofloodpredict
psql geofloodpredict -c "CREATE EXTENSION IF NOT EXISTS postgis;"

# Update .env
DATABASE_URL=postgresql://user:password@localhost/geofloodpredict
```

### Alembic Migrations

```bash
# Generate new migration (after model changes)
uv run alembic revision --autogenerate -m "migration description"

# Apply all pending migrations
uv run alembic upgrade head

# Rollback one migration
uv run alembic downgrade -1
```

---

## 🐳 Docker Setup (Optional)

For local development:

```bash
# Compose file coming in Phase 1
docker-compose up -d

# Creates: PostgreSQL 15 + PostGIS, Redis, auto-initialized DB
```

---

## 📊 Monitoring & Debugging

### Structured Logging

The app uses `loguru` for structured, colored logging:

```python
from loguru import logger

logger.info("Ingesting DEM data...")
logger.error("Failed to fetch data", error=e)
```

### MLflow Experiment Tracking

Track model experiments and compare metrics:

```bash
uv run mlflow ui --host 0.0.0.0 --port 5000
# Access at http://localhost:5000
```

---

## 🧪 Testing

### Running Tests

```bash
# All tests
uv run pytest

# Specific test file
uv run pytest tests/unit/test_health.py -v

# With coverage report
uv run pytest --cov=app --cov-report=term-missing

# Run on file changes
uv run ptw
```

### Test Structure

- `tests/unit/` - Unit tests for isolated components
- `tests/integration/` - Integration tests for workflows (TODO: Phase 1+)

### Example Test

```python
# tests/unit/test_example.py
from fastapi.testclient import TestClient
from app.main import app

def test_health_endpoint():
    client = TestClient(app)
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

---

## 🤝 Contributing

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes and add tests:**
   ```bash
   # Add your code
   # Write tests in tests/unit/ or tests/integration/
   ```

3. **Ensure quality checks pass:**
   ```bash
   uv run pytest tests/ -q
   uv run ruff check . --fix
   uv run mypy app
   ```

4. **Commit with clear messages:**
   ```bash
   git commit -m "Feature: Add flood data ingestion service"
   ```

5. **Push and create PR:**
   ```bash
   git push origin feature/your-feature-name
   ```

---

## 📚 Resources & References

### Geospatial Libraries
- [GeoPandas](https://geopandas.org/) - Vector data processing
- [Rasterio](https://rasterio.readthedocs.io/) - Raster data I/O
- [Rioxarray](https://corteva.github.io/rioxarray/) - Raster with xarray
- [Shapely](https://shapely.readthedocs.io/) - Geometric operations
- [PostGIS](https://postgis.net/) - Spatial database

### Machine Learning
- [Scikit-learn](https://scikit-learn.org/) - ML models
- [XGBoost](https://xgboost.readthedocs.io/) - Gradient boosting
- [Optuna](https://optuna.org/) - Hyperparameter optimization
- [MLflow](https://mlflow.org/) - Experiment tracking

### FastAPI & Backend
- [FastAPI](https://fastapi.tiangelo.com/) - Web framework
- [SQLModel](https://sqlmodel.tiangolo.com/) - SQL ORM
- [Alembic](https://alembic.sqlalchemy.org/) - Database migrations
- [Pydantic](https://docs.pydantic.dev/) - Data validation

### Development Tools
- [UV](https://github.com/astral-sh/uv) - Fast Python package manager
- [Pytest](https://docs.pytest.org/) - Testing framework
- [Ruff](https://docs.astral.sh/ruff/) - Python linter
- [Mypy](https://www.mypy-lang.org/) - Static type checker

---

## 📞 Questions & Support

- 📖 Read [PROJECT_PLAN.md](PROJECT_PLAN.md) for detailed roadmap
- 🐛 Open an issue on GitHub
- 💬 Check inline TODO comments in code
- 🔍 Review docstrings and type hints
