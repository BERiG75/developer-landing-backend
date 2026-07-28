from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.logger import get_logger
from app.exceptions.base import ApplicationException
from app.schemas.error import ErrorDetail, ErrorResponse

logger = get_logger(__name__)


def register_exception_handlers(application: FastAPI) -> None:
    @application.exception_handler(ApplicationException)
    async def application_exception_handler(
        request: Request,
        exc: ApplicationException,
    ) -> JSONResponse:
        logger.warning(
            "Application exception. Path=%s Code=%s Message=%s",
            request.url.path,
            exc.code,
            exc.message,
        )

        response = ErrorResponse(
            detail=ErrorDetail(
                code=exc.code,
                message=exc.message,
            )
        )

        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump(),
        )

    @application.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        logger.warning(
            "Validation failed. Path=%s Errors=%s",
            request.url.path,
            exc.errors(),
        )

        response = ErrorResponse(
            detail=ErrorDetail(
                code="VALIDATION_ERROR",
                message="Request validation failed.",
            )
        )

        return JSONResponse(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            content=response.model_dump(),
        )

    @application.exception_handler(Exception)
    async def unhandled_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        logger.exception(
            "Unhandled exception. Path=%s",
            request.url.path,
        )

        response = ErrorResponse(
            detail=ErrorDetail(
                code="INTERNAL_SERVER_ERROR",
                message="Internal server error.",
            )
        )

        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content=response.model_dump(),
        )
    