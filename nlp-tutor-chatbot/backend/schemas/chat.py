from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Request schema for the Chat API.
    """

    question: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="User's question for the NLP Tutor"
    )


class ChatResponse(BaseModel):
    """
    Response schema for the Chat API.
    """

    agent: str = Field(
        ...,
        description="Agent selected to answer the question (theory/practical)"
    )

    answer: str = Field(
        ...,
        description="AI-generated response"
    )