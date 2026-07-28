from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.log_config import configure_logging
from app.core.logger import get_logger


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None]:
    configure_logging()

    logger = get_logger(__name__)
    logger.info("Application startup completed.")

    try:
        yield
    finally:
        logger.info("Application shutdown completed.")
