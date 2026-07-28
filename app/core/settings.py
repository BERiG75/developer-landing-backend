from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from .constants import APP_VERSION, APP_NAME, APP_DESCRIPTION

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = Field(default=APP_NAME)
    app_version: str = Field(default=APP_VERSION)
    app_description: str = Field(default=APP_DESCRIPTION)
    debug: bool = Field(default=False)

    app_host: str = Field(default="0.0.0.0")
    app_port: int = Field(default=80)

    openai_api_key: str = Field(default="")

    smtp_host: str = Field(default="")
    smtp_port: int = Field(default=587)
    smtp_username: str = Field(default="")
    smtp_password: str = Field(default="")

    mail_from: str = Field(default="")
    mail_to: str = Field(default="")
