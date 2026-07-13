class PromptBuilder:
    """
    Builds prompts for the LLM using
    retrieved context and the user's question.
    """

    @staticmethod
    def build(question: str, chunks: list[dict]) -> str:

        context = ""

        for chunk in chunks:

            context += (
                f"\nTitle: {chunk['title']}\n"
                f"{chunk['text']}\n"
            )

        prompt = f"""
You are an expert NLP professor.

Answer ONLY using the provided context.

If the answer is not present in the context,
reply with:

"I don't have enough information in my knowledge base."

---------------------------------------

Context:

{context}

---------------------------------------

Question:

{question}

---------------------------------------

Answer:
"""

        return prompt