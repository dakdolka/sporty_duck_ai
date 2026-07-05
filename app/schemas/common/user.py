from pydantic import BaseModel

class UserInfo(BaseModel):

    id: str

    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None

    language_code: str | None = None