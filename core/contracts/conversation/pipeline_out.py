from pydantic import BaseModel


class ConversationPipelineOut(BaseModel):
    response_text: str