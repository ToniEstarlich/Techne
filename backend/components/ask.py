import json

import ollama

from backend.config import OLLAMA_MODEL, SYSTEM_PROMPT


def ask_ollama(user_prompt: str) -> dict:
    """Ask the local Ollama model for a structured JSON response."""

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        format="json",
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)

    except json.JSONDecodeError as error:
        print("\nTechne received invalid JSON from Ollama.")
        print(f"JSON error: {error}")
        print("\nRaw Ollama response:")
        print(content)

        raise