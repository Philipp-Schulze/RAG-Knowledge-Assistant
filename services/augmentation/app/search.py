import os
import requests

def fetch_webcrawler_results(query: str) -> str:

    # api details from env
    api_key = os.getenv("TAVILY_API_KEY")
    url = os.getenv("TAVILY_URL")

    # payload structure
    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "basic",            
        "include_answer": False
    }    

    # handle response and format for LLM
    try:
        
        # get response with timeout
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        
        # Format results into a clean string for the LLM
        results = data.get("results", [])
        web_context = "\n".join([f"Source: {r['title']}\nContent: {r['content']}\n" for r in results[:3]])
        return web_context
    
    except Exception as e:

        # error handling
        print(f"[TAVILY ERROR] {e}")
        return ""