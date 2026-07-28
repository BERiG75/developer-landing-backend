from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.common.validators import CommentStr, NameStr, PhoneStr
from app.schemas.common.response import MessageResponse

class ContactRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    name: NameStr = Field(
        ...,
        examples=["John Smith"],
        description="Sender name.",
    )

    email: EmailStr = Field(
        ...,
        examples=["john@example.com"],
        description="Sender email address.",
    )

    phone: PhoneStr | None = Field(
        default=None,
        examples=["+44 7700 900123"],
        description="Sender phone number.",
    )

    comment: CommentStr = Field(
        ...,
        examples=["I'd like to discuss a backend project."],
        description="Message from the sender.",
    )


class ContactResponse(MessageResponse):
    """
    Response returned after a successful contact request.
    """
    