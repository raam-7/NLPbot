class LLMFactory:
    PROVIDER = "huggingface"

    @classmethod
    def create(cls):
        if cls.PROVIDER == "huggingface":
            from services.llm.huggingface_service import HuggingFaceService

            return HuggingFaceService()

        from services.llm.ollama_service import OllamaService

        return OllamaService()
