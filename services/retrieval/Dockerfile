FROM python:3.11-slim
# Grab uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1. Copy workspace metadata and the shared library
# This is required for uv to "see" the workspace members
COPY pyproject.toml uv.lock /app/
COPY shared/ /app/shared/

# 2. Copy the retrieval service code
COPY services/retrieval/ /app/services/retrieval/

# 3. Install both shared and retrieval into system python
# uv automatically handles the workspace link to 'shared'
RUN uv pip install --system ./shared ./services/retrieval

# 4. Set the working directory to the service folder for execution
WORKDIR /app/services/retrieval

# Run the retrieval service
CMD ["python", "main.py"]