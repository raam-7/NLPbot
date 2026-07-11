from sqlalchemy import select
from sqlalchemy.orm import Session

from models.conversation import Conversation


class ConversationRepository:
    """
    Handles all database operations related to conversations.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        user_id: int,
        title: str,
    ) -> Conversation:
        """
        Create a new conversation.
        """

        conversation = Conversation(
            user_id=user_id,
            title=title,
        )

        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)

        return conversation

    def get_by_id(
        self,
        conversation_id: int,
    ) -> Conversation | None:
        """
        Get a conversation by ID.
        """

        statement = select(Conversation).where(
            Conversation.id == conversation_id
        )

        return self.db.execute(statement).scalar_one_or_none()

    def get_all_by_user(
        self,
        user_id: int,
    ) -> list[Conversation]:
        """
        Get all conversations for a user.
        """

        statement = (
            select(Conversation)
            .where(Conversation.user_id == user_id)
            .order_by(Conversation.updated_at.desc())
        )

        return list(
            self.db.execute(statement).scalars().all()
        )

    def delete(
        self,
        conversation: Conversation,
    ) -> None:
        """
        Delete a conversation.
        """

        self.db.delete(conversation)
        self.db.commit()