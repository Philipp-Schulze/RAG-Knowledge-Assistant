import os
import time
import logging
import requests
from typing import Any

logger = logging.getLogger(__name__)

MODEL_REGISTRY = {
    "summarizer": os.getenv("MODEL_SUMMARIZER"),
    "judge": os.getenv("MODEL_JUDGE"),
    "generator": os.getenv("MODEL_GENERATOR")
    }

def call_model(task: str, prompt: str, max_tokens: int, stream: bool = False) -> Any:

    # initialize model based on task
    model_name = MODEL_REGISTRY.get(task)
    url = os.getenv('OLLAMA_URL')

    # payload structure
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": stream,
        "options": {"num_predict": max_tokens}
    }

    logger.info(f"[LLM IN] task={task} model={model_name} max_tokens={max_tokens} prompt={prompt!r}")

    # We use stream=stream in the request call to handle the response body correctly
    # Generous timeout: CPU inference for larger models (e.g. qwen2.5:7b) can take well over 60s
    call_start = time.time()
    response = requests.post(url, json=payload, stream=stream, timeout=300)

    response.raise_for_status()

    if not stream:
        result = response.json().get("response", "").strip()
        logger.info(f"[TIMER] call_model task={task} model={model_name} (models.py): {time.time() - call_start:.3f}s")
        logger.info(f"[LLM OUT] task={task} model={model_name} response={result!r}")
        return result

    logger.info(f"[TIMER] call_model task={task} model={model_name} (models.py, stream init): {time.time() - call_start:.3f}s")
    return response