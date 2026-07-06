from pydantic import BaseModel


class ResolveIdentityRequest(BaseModel):
    telegram_user_id: int

    username: str | None
    first_name: str
    last_name: str | None
    language_code: str | None