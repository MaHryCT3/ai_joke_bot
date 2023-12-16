from datetime import datetime

from sqlalchemy import BigInteger, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base import BaseModel


class JokeTable(BaseModel):
    __tablename__ = "joke"

    text = mapped_column(
        String,
        nullable=False,
    )

    author_telegram_id = mapped_column(
        BigInteger,
        nullable=True,
    )

    is_created_by_admin: Mapped[bool] = mapped_column(
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
        server_default=func.now(),
    )
