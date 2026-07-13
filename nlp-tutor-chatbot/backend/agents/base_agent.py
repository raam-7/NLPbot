from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Abstract base class for all AI agents.

    Every agent in the system must implement
    the handle() method.
    """

    @abstractmethod
    def handle(self, question: str) -> str:
        """
        Process the user's question and return a response.
        """
        pass