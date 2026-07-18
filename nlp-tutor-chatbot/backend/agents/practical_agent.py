from agents.base_agent import BaseAgent
from rag.retriever import Retriever
from rag.prompt_builder import PromptBuilder
from services.llm.factory import LLMFactory


class PracticalAgent(BaseAgent):
    """
    Handles practical NLP questions.
    """

    def __init__(self):
        print("✅ Practical Agent Initialized")

        self.retriever = Retriever("practical")
        self.llm = LLMFactory.create()

    def handle(self, question: str) -> str:

        chunks = self.retriever.search(question)

        if not chunks:
            return "I don't have enough practical information in my knowledge base."

        prompt = PromptBuilder.build(question, chunks)

        answer = self.llm.generate(prompt)

        return answer


if __name__ == "__main__":

    agent = PracticalAgent()

    while True:

        question = input("\nAsk a practical question: ")

        if question.lower() in ["exit", "quit"]:
            break

        print("\n")

        print(agent.handle(question))