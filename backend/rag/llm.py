from ollama import chat

def ask_llm(prompt: str) -> str:
    response = chat(
        model="phi4-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content