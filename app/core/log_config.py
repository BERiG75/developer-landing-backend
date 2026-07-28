from logging.config import dictConfig
from pathlib import Path

from app.core.config import settings

LOG_DIRECTORY = Path("storage/logs")

APPLICATION_LOG = LOG_DIRECTORY / "application.log"

ERROR_LOG = LOG_DIRECTORY / "errors.log"


def configure_logging() -> None:
    LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": (
                        "%(asctime)s | "
                        "%(levelname)s | "
                        "%(name)s | "
                        "%(message)s"
                    ),
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                },
                "application_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "default",
                    "filename": str(APPLICATION_LOG),
                    "maxBytes": settings.log_max_bytes,
                    "backupCount": settings.log_backup_count,
                    "encoding": "utf-8",
                },
                "error_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "default",
                    "filename": str(ERROR_LOG),
                    "level": "ERROR",
                    "maxBytes": settings.log_max_bytes,
                    "backupCount": settings.log_backup_count,
                    "encoding": "utf-8",
                },
            },
            "root": {
                "level": settings.log_level.value,
                "handlers": [
                    "console",
                    "application_file",
                    "error_file",
                ],
            },
        }
    )
    