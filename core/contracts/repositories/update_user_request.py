from uuid import UUID

from pydantic import BaseModel


class UpdateUserRequest(BaseModel):
    user_id: UUID

    username: str | None
    first_name: str
    last_name: str | None

    language_code: str | None   