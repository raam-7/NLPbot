from fastapi import APIRouter, HTTPException

from agents.router import RouterAgent
from schemas.chat import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

# Create the router agent once when the application starts
router_agent = RouterAgent()


@router.post(
    "/",
    response_model=ChatResponse,
    summary="Chat with the NLP Tutor"
)
def chat(request: ChatRequest):
    """
    Handles user questions using the Multi-Agent NLP Tutor.
    """

    try:
        answer = router_agent.route(request.question)

        # Detect which agent handled the request
        practical_keywords = RouterAgent.PRACTICAL_KEYWORDS

        selected_agent = "theory"

        if any(keyword in request.question.lower() for keyword in practical_keywords):
            selected_agent = "practical"

        return ChatResponse(
            agent=selected_agent,
            answer=answer
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )