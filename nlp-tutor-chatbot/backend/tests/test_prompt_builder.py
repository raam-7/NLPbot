from rag.prompt_builder import PromptBuilder

chunks = [
    {
        "title": "Tokenization",
        "text": "Tokenization is the process of splitting text into tokens."
    }
]

prompt = PromptBuilder.build(
    "What is Tokenization?",
    chunks,
)

print(prompt)