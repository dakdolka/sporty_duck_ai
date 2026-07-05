from pydantic import BaseModel

from app.schemas.common import EventInfo, UserInfo


class HelpRequest(BaseModel):
    user: UserInfo
    event: EventInfo


class HelpResponse(BaseModel):
    text: str