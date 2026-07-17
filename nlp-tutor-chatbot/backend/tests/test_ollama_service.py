from services.llm.ollama_service import OllamaService

llm = OllamaService()

response = llm.generate(
    "In one sentence, what is Tokenization?"
)

print("\nModel Response:\n")
print(response)