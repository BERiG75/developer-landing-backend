from time import perf_counter

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.core.logger import get_logger

logger = get_logger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:
        start = perf_counter()

        response = await call_next(request)

        duration = (perf_counter() - start) * 1000

        logger.info(
            (
                "Client=%s | "
                "Method=%s | "
                "Path=%s | "
                "Status=%d | "
                "Duration=%.2f ms"
            ),
            request.client.host if request.client else "-",
            request.method,
            request.url.path,
            response.status_code,
            duration,
        )

        return response
    