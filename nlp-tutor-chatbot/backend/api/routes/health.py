from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to the NLP Tutor Chatbot API!"
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "NLP Tutor Chatbot Backend"
    }