from app.models import call_model

def compress_context(context: str, mode: str) -> str:

    # Fast mode: Simple truncation
    if mode == "fast":
        return context[:800] + "..."
    
    # Complex mode: Semantic compression via SLMon.
    elif mode == "complex":
        return _summarize(context)

    return context

def _summarize(context: str) -> str:

    # Prepare prompt
    prompt = f"You are an expert summarizer. Extract only the most important technical facts from the following text.\nContext: {context}"
    
    # call summarizer model
    return call_model(
        task="summarizer",
        prompt=prompt,
        max_tokens=300,
        stream=False
    )