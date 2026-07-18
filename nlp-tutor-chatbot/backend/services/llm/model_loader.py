import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class ModelLoader:
    _model = None
    _tokenizer = None

    MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"

    @classmethod
    def load(cls):
        if cls._model is None:
            print(f"Loading {cls.MODEL_NAME}...")

            cls._tokenizer = AutoTokenizer.from_pretrained(
                cls.MODEL_NAME
            )

            cls._model = AutoModelForCausalLM.from_pretrained(
                cls.MODEL_NAME,
                torch_dtype=torch.float16,
                device_map="auto",
            )

            print("✅ Model loaded successfully.")

        return cls._model, cls._tokenizer