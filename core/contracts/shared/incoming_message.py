from datetime import datetime

from pydantic import BaseModel


class IncomingMessage(BaseModel):
    message_id: int
    sent_at: datetime
    text: str | None    