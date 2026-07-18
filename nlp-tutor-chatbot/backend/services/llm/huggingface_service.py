import torch

from services.llm.base import BaseLLM
from services.llm.model_loader import ModelLoader


class HuggingFaceService(BaseLLM):

    def __init__(self):
        self.model, self.tokenizer = ModelLoader.load()

    def generate(self, prompt: str) -> str:

        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
        ).to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=512,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
            )

        generated_ids = outputs[:, inputs["input_ids"].shape[1]:]

        answer = self.tokenizer.batch_decode(
            generated_ids,
            skip_special_tokens=True,
        )[0].strip()

        return answer