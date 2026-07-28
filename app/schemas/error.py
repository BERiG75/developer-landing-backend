from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    code: str = Field(
        ...,
        description="Error code.",
        examples=["VALIDATION_ERROR"],
    )
    message: str = Field(
        ...,
        description="Error message.",
        examples=["Validation failed."],
    )


class ErrorResponse(BaseModel):
    detail: ErrorDetail
