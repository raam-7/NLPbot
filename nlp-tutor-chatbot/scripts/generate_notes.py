from ollama import chat

response = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Explain Tokenization in NLP with a definition and one simple example."
        }
    ]
)

print(response["message"]["content"])