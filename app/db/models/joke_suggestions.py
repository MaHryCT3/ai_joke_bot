from datetime import datetime

from sqlalchemy import BigInteger, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base import BaseModel


class JokeSuggestionTable(BaseModel):
    __tablename__ = "joke_suggestion"

    text = mapped_column(
        String,
        nullable=False,
    )

    telegram_id = mapped_column(
        BigInteger,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
        server_default=func.now(),
    )

    is_approved: Mapped[bool] = mapped_column(
        nullable=True,
    )
