from services.llm.base import BaseLLM

try:
    from ollama import chat
except ImportError:  # pragma: no cover - depends on optional local install
    chat = None


class OllamaService(BaseLLM):
    def __init__(self, model="qwen3:4b"):
        self.model = model

    def generate(self, prompt: str) -> str:
        if chat is None:
            raise RuntimeError(
                "The optional 'ollama' package is not installed. "
                "Install it with 'pip install ollama' to use OllamaService."
            )

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]
