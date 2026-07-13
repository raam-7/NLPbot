class RouterAgent:
    """
    Decides which agent should handle the user's question.
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

    def route(self, question: str) -> str:

        question = question.lower()

        for keyword in self.PRACTICAL_KEYWORDS:

            if keyword in question:
                return "practical"

        return "theory"


if __name__ == "__main__":

    router = RouterAgent()

    while True:

        question = input("\nAsk a question: ")

        agent = router.route(question)

        print(f"\nSelected Agent: {agent}")