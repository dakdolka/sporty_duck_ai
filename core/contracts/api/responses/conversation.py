from pydantic import BaseModel


class ConversationResponse(BaseModel):
    text: str