def apply_mode(context: str, mode: str) -> str:

    # fast mode
    if mode == "fast":
        return f"Fasse kurz zusammen: {context}"
    # complex mode
    else:
        return f"Wende Chain of Thought an und verstehe schrittweise: {context}"

def build_prompt(query: str, context: str, role: str, mode: str) -> str:


    # dictionary of roles
    roles  = {
        "technical": "Du bist ein Experte.",
        "creative": "Sei kreativ.",
        "defensive": "Vermeide Risiken und sei vorsichtig.",
        "concise": "Sei kurz und prägnant.",
        "detailed": "Gib eine ausführliche Antwort."
    }

    # get mode
    role = roles.get(role, "Du bist ein hilfreicher Assistent.")
    
    # get strategy
    strategy = apply_mode(context, mode)

    # always answer in the language of the query
    language_instruction = "Antworte in der Sprache, in der die Frage gestellt wurde."

    # 3. Combine into the final system prompt structure
    return f"{role}\n\n{language_instruction}\n\n{strategy}\n\nFrage: {query}"