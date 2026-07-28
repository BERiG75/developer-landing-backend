from pydantic import BaseModel, ConfigDict, Field


class MessageResponse(BaseModel):
    """
    Generic response containing only a message.
    """

    model_config = ConfigDict(
        frozen=True,
    )

    message: str = Field(
        ...,
        description="Response message.",
        examples=["Operation completed successfully."],
    )
