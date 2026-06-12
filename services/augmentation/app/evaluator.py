from typing import List, Tuple

from shared.schemas import Chunk, SourceReference

from app.search import fetch_webcrawler_results

def _calculate_weighted_confidence(chunks: List[Chunk]) -> float:

    # If no chunks, return 0.0
    if not chunks: 
        return 0.0
    # Weight: Top chunk gets 1.0, second gets 0.5, etc.
    weights = [1 / (i + 1) for i in range(len(chunks))]
    weighted_scores = [c.confidence_score * w for c, w in zip(chunks, weights)]
    return sum(weighted_scores) / sum(weights)

def run_evaluation_pipeline(query: str, chunks: List[Chunk], threshold: float = 4.0) -> Tuple[str, List[SourceReference], float]:
    
    # 1. Filter & Sort
    confident_chunks = [c for c in chunks if c.confidence_score >= threshold]
    confident_chunks.sort(key=lambda x: x.confidence_score, reverse=True)
    
    # 2. Build Context
    context = "\n".join([c.content for c in confident_chunks])
    
    # 3. Handle References and Confidence
    if confident_chunks:
        references = [
            SourceReference(
                file_name=c.file_name, 
                author=c.author, 
                confidence_score=c.confidence_score
            ) 
            for c in confident_chunks
        ]
        # Use the weighted helper
        agg_conf = _calculate_weighted_confidence(confident_chunks)

    else:
        
        # 4. Fallback Logic (if no internal chunks pass threshold)
        print("[CURATOR] Internal confidence low. Triggering Tavily fallback...")
        context = fetch_webcrawler_results(query)
        
        # Define web search reference
        references = [
            SourceReference(
                file_name="Tavily Web Search", 
                author="AI Crawler", 
                confidence_score=0.0
            )
        ]
        agg_conf = 0.0
        
    return context, references, agg_conf