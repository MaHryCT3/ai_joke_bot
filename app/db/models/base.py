from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, mapped_column


class BaseModel(DeclarativeBase):
    __abstract__ = True

    id = mapped_column(
        BigInteger,
        primary_key=True,
    )
