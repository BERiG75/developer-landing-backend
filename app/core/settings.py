from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from app.core.constants import APP_VERSION, APP_NAME, APP_DESCRIPTION
from app.common.enums import LogLevel

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

    log_level: LogLevel = Field(default=LogLevel.INFO)
    log_max_bytes: int = Field(default=5 * 1024 * 1024)
    log_backup_count: int = Field(default=5)

    openai_api_key: str = Field(default="")

    smtp_host: str = Field(default="")
    smtp_port: int = Field(default=587)
    smtp_username: str = Field(default="")
    smtp_password: str = Field(default="")

    mail_from: str = Field(default="")
    mail_to: str = Field(default="")
