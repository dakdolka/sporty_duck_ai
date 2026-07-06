from datetime import datetime

from pydantic import BaseModel

class MessageRequest(BaseModel):
    user_telegram_id: int
    text: str
    sent_at: datetime
    language_code: str | None = None
    last_name: str | None = None
    first_name: str | None = None
    username: str | None = None
    chat_id: str | None = None
    
    
class MessageResponse(BaseModel):
    message: str