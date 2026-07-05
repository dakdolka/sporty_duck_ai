from datetime import datetime

from pydantic import BaseModel


class EventInfo(BaseModel):
    chat_id: str
    message_id: str
    sent_at: datetime
    text: str | None = None