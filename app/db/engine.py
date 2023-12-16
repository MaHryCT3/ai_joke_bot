from sqlalchemy import URL, create_engine

from app.config import settings

POSTGRES_URL = URL.create(
    "postgresql",
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    database=settings.POSTGRES_DB,
)


engine = create_engine(POSTGRES_URL, echo=True)
