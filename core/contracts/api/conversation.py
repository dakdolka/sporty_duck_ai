from pydantic import BaseModel

from core.contracts.common import EventInfo, UserInfo


class ConversationRequest(BaseModel):
    user: UserInfo
    event: EventInfo


class ConversationResponse(BaseModel):
    message: str