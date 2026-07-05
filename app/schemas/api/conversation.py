from pydantic import BaseModel

from app.schemas.common import EventInfo, UserInfo


class ConversationRequest(BaseModel):
    user: UserInfo
    event: EventInfo


class ConversationResponse(BaseModel):
    message: str