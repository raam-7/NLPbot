from datetime import datetime

from pydantic import BaseModel


class ConversationCreate(BaseModel):
    """
    Request schema for creating a conversation.
    """

    title: str


class ConversationResponse(BaseModel):
    """
    Response schema for a conversation.
    """

    id: int
    user_id: int
    title: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }