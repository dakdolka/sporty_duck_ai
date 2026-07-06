from pydantic import BaseModel


class ConversationOrchestratorResponse(BaseModel):
    text: str