from fastapi import FastAPI
from api.routes.conversation import router as conversation_router
from api.routes.auth import router as auth_router

app = FastAPI(
    title="AI-Powered NLP Tutor Chatbot",
    version="1.0.0",
)
app.include_router(auth_router)
app.include_router(conversation_router)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the NLP Tutor Chatbot API!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "NLP Tutor Chatbot Backend",
    }