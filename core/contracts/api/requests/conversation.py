from pydantic import BaseModel

from contracts.shared.incoming_message import IncomingMessage


class ConversationRequest(BaseModel):
    telegram_user_id: int

    username: str | None
    first_name: str
    last_name: str | None
    language_code: str | None

    message: IncomingMessage