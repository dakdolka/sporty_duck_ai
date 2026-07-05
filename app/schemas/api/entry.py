from pydantic import BaseModel

from app.schemas.common import EventInfo, UserInfo


class EntryRequest(BaseModel):
    user: UserInfo
    event: EventInfo


class EntryResponse(BaseModel):
    message: str