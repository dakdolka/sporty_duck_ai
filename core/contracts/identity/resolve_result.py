from uuid import UUID

from pydantic import BaseModel


class ResolvedIdentity(BaseModel):
    user_id: UUID

    first_name: str

    is_new: bool