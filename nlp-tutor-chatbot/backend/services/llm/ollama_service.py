from ollama import chat


class OllamaService:
    """
    Handles communication with the local Ollama server.
    """

    def __init__(self, model: str = "qwen3:4b"):
        self.model = model

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to Ollama and return the model's response.
        """

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]