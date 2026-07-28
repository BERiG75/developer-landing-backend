from pydantic import BaseModel, ConfigDict, Field


class MetricsResponse(BaseModel):
    """
    Contact form statistics.
    """

    model_config = ConfigDict(
        frozen=True,
    )

    total_requests: int = Field(
        ge=0,
        description="Total number of contact requests.",
        examples=[25],
    )

    successful_requests: int = Field(
        ge=0,
        description="Successfully processed contact requests.",
        examples=[23],
    )

    failed_requests: int = Field(
        ge=0,
        description="Failed contact requests.",
        examples=[2],
    )
    