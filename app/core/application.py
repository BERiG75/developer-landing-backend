from fastapi import FastAPI

from app.api.router import api_router
from app.core.constants import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
)


def create_application() -> FastAPI:
    application = FastAPI(
        title=APP_TITLE,
        description=APP_DESCRIPTION,
        version=APP_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    application.include_router(api_router)

    return application
