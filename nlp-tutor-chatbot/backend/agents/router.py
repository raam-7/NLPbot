from agents.theory_agent import TheoryAgent
from agents.practical_agent import PracticalAgent


class RouterAgent:
    """
    Routes the user's question to the correct AI agent.
    """

    PRACTICAL_KEYWORDS = {
        "code",
        "python",
        "program",
        "implement",
        "implementation",
        "write",
        "script",
        "example",
        "coding",
        "project",
        "build",
        "develop",
        "train",
        "library",
        "api",
    }

    def __init__(self):
        # Create one instance of each agent
        self.theory_agent = TheoryAgent()
        self.practical_agent = PracticalAgent()

    def route(self, question: str) -> str:

        question_lower = question.lower()

        for keyword in self.PRACTICAL_KEYWORDS:
            if keyword in question_lower:
                print("\n📌 Routing to Practical Agent...\n")
                return self.practical_agent.handle(question)

        print("\n📘 Routing to Theory Agent...\n")
        return self.theory_agent.handle(question)


if __name__ == "__main__":

    router = RouterAgent()

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() in ["exit", "quit"]:
            break

        answer = router.route(question)

        print("\n" + "=" * 80)
        print(answer)
        print("=" * 80)