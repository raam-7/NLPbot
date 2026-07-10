from fastapi import FastAPI

from api.routes.health import router as health_router
from core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

app.include_router(health_router)