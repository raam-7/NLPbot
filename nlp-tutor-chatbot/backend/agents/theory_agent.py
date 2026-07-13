from agents.base_agent import BaseAgent
from rag.retriever import Retriever


class TheoryAgent(BaseAgent):
    """
    Handles theoretical NLP questions.
    """

    def __init__(self):
        print("✅ Theory Agent Initialized")

        self.retriever = Retriever("theory")

    def handle(self, question: str) -> str:
        """
        Retrieve relevant theory chunks.
        """

        results = self.retriever.search(question)

        if not results:
            return "No relevant information found."

        response = []

        response.append("=" * 60)
        response.append("Retrieved Theory Chunks")
        response.append("=" * 60)

        for i, result in enumerate(results, start=1):

            response.append(f"\nChunk {i}")

            response.append(f"Title : {result['title']}")

            response.append(f"Source : {result['source']}")

            response.append(f"Distance : {result['score']:.4f}")

            response.append(result["text"][:300])

            response.append("-" * 60)

        return "\n".join(response)


if __name__ == "__main__":

    agent = TheoryAgent()

    while True:

        question = input("\nAsk a theory question: ")

        answer = agent.handle(question)

        print("\n")

        print(answer)