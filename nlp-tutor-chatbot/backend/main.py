from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.auth import router as auth_router
from api.routes.conversation import router as conversation_router
from api.routes.chat import router as chat_router

app = FastAPI(
    title="AI-Powered NLP Tutor Chatbot",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(conversation_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the NLP Tutor Chatbot API!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "NLP Tutor Chatbot Backend"
    }