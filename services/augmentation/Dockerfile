# docker image
FROM python:3.11-slim

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# set workdir and copy files
WORKDIR /app
COPY . .

# install dependencies
RUN uv pip install --system ./shared ./services/augmentation

# set environment variable for python path and workdir for the service
ENV PYTHONPATH=/app/services/augmentation
WORKDIR /app/services/augmentation

# run the service
CMD ["python", "app/main.py"]