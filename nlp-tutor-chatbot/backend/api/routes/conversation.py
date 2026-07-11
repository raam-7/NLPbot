
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.conversations import (
    ConversationCreate,
    ConversationResponse,
)
from services.conversation_service import ConversationService

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)

# Temporary user until JWT authentication is connected
DEMO_USER_ID = 1


@router.post(
    "",
    response_model=ConversationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_conversation(
    conversation: ConversationCreate,
    db: Session = Depends(get_db),
):
    service = ConversationService(db)

    return service.create_conversation(
        user_id=DEMO_USER_ID,
        title=conversation.title,
    )


@router.get(
    "",
    response_model=list[ConversationResponse],
)
def get_conversations(
    db: Session = Depends(get_db),
):
    service = ConversationService(db)

    return service.get_user_conversations(
        DEMO_USER_ID
    )


@router.get(
    "/{conversation_id}",
    response_model=ConversationResponse,
)
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
):
    service = ConversationService(db)

    try:
        return service.get_conversation(
            conversation_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete(
    "/{conversation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
):
    service = ConversationService(db)

    try:
        service.delete_conversation(
            conversation_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
