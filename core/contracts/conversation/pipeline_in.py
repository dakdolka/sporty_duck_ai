from uuid import UUID

from pydantic import BaseModel

from core.contracts.shared.incoming_message import IncomingMessage


class ConversationPipelineIn(BaseModel):
    user_id: UUID

    first_name: str

    message: IncomingMessage