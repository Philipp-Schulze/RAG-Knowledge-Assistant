FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1. Copy workspace metadata and shared library
COPY pyproject.toml uv.lock /app/
COPY shared/ /app/shared/

# 2. Copy the ingestion service code
COPY services/ingestion/ /app/services/ingestion/

# 3. Use uv to install everything into the system Python
# This handles the workspace 'shared' link automatically
RUN uv pip install --system ./shared ./services/ingestion

# Change to service directory
WORKDIR /app/services/ingestion

# Run the worker
CMD ["python", "worker.py"]