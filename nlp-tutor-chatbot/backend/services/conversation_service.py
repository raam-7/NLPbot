from sqlalchemy.orm import Session

from models.conversation import Conversation
from repositories.conversation_repository import ConversationRepository


class ConversationService:
    """
    Business logic for conversations.
    """

    def __init__(self, db: Session):
        self.repository = ConversationRepository(db)

    def create_conversation(
        self,
        user_id: int,
        title: str,
    ) -> Conversation:
        """
        Create a new conversation.
        """

        return self.repository.create(
            user_id=user_id,
            title=title,
        )

    def get_conversation(
        self,
        conversation_id: int,
    ) -> Conversation:
        """
        Get a conversation by ID.
        """

        conversation = self.repository.get_by_id(
            conversation_id
        )

        if not conversation:
            raise ValueError("Conversation not found.")

        return conversation

    def get_user_conversations(
        self,
        user_id: int,
    ) -> list[Conversation]:
        """
        Get all conversations for a user.
        """

        return self.repository.get_all_by_user(user_id)

    def delete_conversation(
        self,
        conversation_id: int,
    ):
        """
        Delete a conversation.
        """

        conversation = self.repository.get_by_id(
            conversation_id
        )

        if not conversation:
            raise ValueError("Conversation not found.")

        self.repository.delete(conversation)