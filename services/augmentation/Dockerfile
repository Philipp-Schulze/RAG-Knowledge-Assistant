FROM python:3.11-slim
# Copy the uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1. Copy workspace configuration and the shared library
# uv needs the root pyproject.toml to resolve the 'shared' source
COPY pyproject.toml uv.lock /app/
COPY shared/ /app/shared/

# 2. Copy the augmentation service code
COPY services/augmentation/ /app/services/augmentation/

# 3. Install the environment into system python
# This installs both 'shared' and 'augmentation' in one efficient step
RUN uv pip install --system ./shared ./services/augmentation

# 4. Set the working directory to the service path
WORKDIR /app/services/augmentation

# Run the augmentation logic
CMD ["python", "main.py"]