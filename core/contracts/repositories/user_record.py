from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserRecord(BaseModel):
    id: UUID

    telegram_user_id: int

    username: str | None
    first_name: str
    last_name: str | None

    language_code: str | None

    created_at: datetime
    updated_at: datetime