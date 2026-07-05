from pydantic import BaseModel

from app.schemas.common import EventInfo, UserInfo

class ConversationPipelineIn(BaseModel):
    user: UserInfo
    event: EventInfo
    
class ConversationPipelineOut(BaseModel):
    llm_answer: str