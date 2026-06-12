import os
import requests
from typing import Any

from app.models import call_model

def get_llm_response(prompt: str, provider: str, max_tokens: int, stream: bool = False) -> Any:
    
    # local mode
    if provider.lower() == "local":
        return call_model(
            task="generator",
            prompt=prompt,
            max_tokens=max_tokens,
            stream=stream
        )
    
    # api mode
    else:

        # prepare api request
        url, payload, headers = _prepare_api_request(prompt, max_tokens, stream)

        # call api
        response = requests.post(url, json=payload, headers=headers, stream=stream, timeout=60)
        response.raise_for_status()

        # return
        return response.json()["choices"][0]["message"]["content"]

def _prepare_api_request(prompt: str, max_tokens: int, stream: bool = False):

    # api details from env
    
    api_key = os.getenv("GEMINI_API_KEY")
    url = os.getenv("GEMINI_URL")
    model = os.getenv("GENERATION_MODEL_API")
    
    # header structure
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # payload structure
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "stream": stream,
        # disable Gemini "thinking" tokens so max_tokens is fully available for the answer
        "extra_body": {"google": {"thinking_config": {"thinking_budget": 0}}}
    }

    return url, payload, headers