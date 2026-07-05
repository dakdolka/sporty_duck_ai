from pydantic import BaseModel

from core.contracts.common import EventInfo, UserInfo

class ConversationPipelineIn(BaseModel):
    user: UserInfo
    event: EventInfo
    
class ConversationPipelineOut(BaseModel):
    llm_answer: str