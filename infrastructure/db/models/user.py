from uuid import UUID, uuid4

from sqlalchemy import BigInteger, Boolean, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from .basemodel import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    telegram_user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
        index=True,
    )

    telegram_chat_id: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    username: Mapped[str | None] = mapped_column(
        String(32),
        nullable=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )

    last_name: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
    )

    language_code: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
    )