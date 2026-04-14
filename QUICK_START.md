# GeoFloodPredict - Quick Reference

## 🚀 One-Liner Commands

```bash
# Start development
cd /home/nikhil/GeoFloodPredict && source .venv/bin/activate && uv run uvicorn app.main:app --reload

# Run tests
uv run pytest tests/ -v

# Check code quality
uv run ruff check . && uv run mypy app

# View API docs
open http://localhost:8000/docs

# Health check
curl http://localhost:8000/api/v1/health | python -m json.tool
```

---

## 📦 Dependency Management

```bash
# Add new runtime package
uv add package-name

# Add new dev-only package
uv add --dev package-name

# List all installed packages
uv pip list

# View dependency tree
uv pip show package-name
```

---

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/unit/test_health.py

# Run with verbose output
uv run pytest -v

# Run with coverage
uv run pytest --cov=app --cov-report=html

# Run tests matching pattern
uv run pytest -k health
```

---

## 💻 Development Workflow

```bash
# 1. Activate environment (if needed)
source .venv/bin/activate

# 2. Start dev server with hot reload
uv run uvicorn app.main:app --reload

# 3. In another terminal, run tests
uv run pytest --watch

# 4. Check code quality before commit
uv run ruff check . --fix
uv run mypy app
```

---

## 🗄️ Database Commands

```bash
# Initialize database (requires PostgreSQL running)
uv run python app/db/session.py

# Create migration after model changes
uv run alembic revision --autogenerate -m "description"

# Apply migrations
uv run alembic upgrade head

# Rollback one migration
uv run alembic downgrade -1
```

---

## 📊 Monitoring

```bash
# MLflow UI (experiment tracking)
uv run mlflow ui --host 0.0.0.0 --port 5000

# API documentation (auto-generated)
# Visit http://localhost:8000/docs while server running
```

---

## 🔧 Common Issues & Fixes

### Tests fail with "No module named asyncpg"
```bash
uv add asyncpg
```

### Linting violations
```bash
uv run ruff check . --fix
```

### Type checking failed
```bash
uv run mypy app --config-file=pyproject.toml
```

### Database connection error
```bash
# Make sure PostgreSQL is running
# Update DATABASE_URL in .env
```

---

## 📚 Useful Links

- **API Running:** http://localhost:8000/docs
- **MLflow Dashboard:** http://localhost:5000 (start with `mlflow ui`)
- **GitHub:** https://github.com/your-org/GeoFloodPredict
- **Project Plan:** See `PROJECT_PLAN.md`
- **Full Roadmap:** See `README.md`

---

## 👥 Helpful Commands for Team

```bash
# Setup for new team member
git clone https://github.com/your-org/GeoFloodPredict.git
cd GeoFloodPredict
uv venv
source .venv/bin/activate
uv sync    # Install exact locked dependencies

# Pre-commit setup
uv run pre-commit install

# Verify setup
uv run pytest
uv run ruff check .

# Start developing
uv run uvicorn app.main:app --reload
```

---

**Last Updated:** April 14, 2026
**Project Version:** 0.1.0 (Phase 0)
