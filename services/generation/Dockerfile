FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1. Copy workspace metadata and shared library
COPY pyproject.toml uv.lock /app/
COPY shared/ /app/shared/

# 2. Copy the generation service code
COPY services/generation/ /app/services/generation/

# 3. Install via uv (system python)
RUN uv pip install --system ./shared ./services/generation

# 4. Set working directory to the service
WORKDIR /app/services/generation

# Run the agent
CMD ["python", "agent.py"]