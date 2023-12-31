import logging
import sys

from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(extra='ignore')  # Игнорирование лишних переменных в env файле

    # Debug
    DEBUG: bool = False

    # Application
    TELEGRAM_TOKEN: str
    MODERATION_CHAT_ID: int
    ERROR_LOG_CHAT_ID: int
    MIN_PERCENT_FOR_JOKE: float = Field(default=0.4, gt=0, lt=1)

    # Database
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str


settings = Settings(_env_file='.env')

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
