from sqlalchemy import create_engine, URL

from app.config import settings


POSTGRES_URL = URL.create(
    'postgresql',
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    database=settings.POSTGRES_DB,
)


engine = create_engine(POSTGRES_URL, echo=True, pool_size=100, max_overflow=200)
