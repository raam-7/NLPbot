from agents.base_agent import BaseAgent
from rag.retriever import Retriever
from rag.prompt_builder import PromptBuilder
from services.llm.factory import LLMFactory


class TheoryAgent(BaseAgent):
    """
    Handles theoretical NLP questions using RAG.
    """

    def __init__(self):
        print("✅ Theory Agent Initialized")

        self.retriever = Retriever("theory")
        self.llm = LLMFactory.create()

    def handle(self, question: str) -> str:

        # Retrieve relevant chunks
        chunks = self.retriever.search(question)

        if not chunks:
            return "I don't have enough information in my knowledge base."

        # Build prompt
        prompt = PromptBuilder.build(question, chunks)

        # Generate answer using Qwen
        answer = self.llm.generate(prompt)

        return answer


if __name__ == "__main__":

    agent = TheoryAgent()

    while True:

        question = input("\nAsk a theory question: ")

        if question.lower() in ["exit", "quit"]:
            break

        answer = agent.handle(question)

        print("\n" + "=" * 70)
        print(answer)
        print("=" * 70)