from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class HealthResponse(BaseModel):
    """
    Health check response.

    Returned by GET /api/health.
    """

    model_config = ConfigDict(
        frozen=True,
    )

    status: Literal["ok"] = Field(
        description="Application health status.",
        examples=["ok"],
    )

    version: str = Field(
        description="Application version.",
        examples=["1.0.0"],
    )

    uptime_seconds: int = Field(
        ge=0,
        description="Application uptime in seconds.",
        examples=[153],
    )
