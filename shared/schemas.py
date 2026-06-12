# Location: shared/schemas.py
from pydantic import BaseModel, Field
from typing import List

class Chunk(BaseModel):

    file_name: str                      # "machine_learning_basics.pdf"
    author: str                         # "John Doe"
    confidence_score: float             # 0.0 - 5.0
    content: str                        # "Machine learning is a subset of ..."

class Settings(BaseModel):
    max_tokens: int = Field(default=500, ge=1000, le=2000)       # 500
    role: str = "technical"                                     # "technical", "concise", "detailed"
    provider: str = "local"                                     # "local" (Ollama), "api" (Gemini API)
    mode: str = "fast"                                          # "fast", "complex"
    threshold: float = 4.0                                      # 4.0    
 
class ChatRequest(BaseModel):

    query: str                                                  # "Was ist RAG?"
    settings: Settings = Field(default_factory=Settings)        # Optional settings with defaults

class SourceReference(BaseModel):

    file_name: str                  # "machine_learning_basics.pdf" or "Tavily Web Search"
    author: str                     # "John Doe"
    confidence_score: float         # 0.0 - 5.0

class ChatResponse(BaseModel):

    answer: str                                 # "RAG steht für ..."
    tokens_used: int                            # 450
    source_documents: List[SourceReference]     # [SourceReference(file_name="machine_learning_basics.pdf", author="John Doe", confidence_score=4.5)]
    aggregated_confidence: float                # 0.0 - 5.0