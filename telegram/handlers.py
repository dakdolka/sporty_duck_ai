from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
import httpx
from aiogram.fsm.state import State, StatesGroup
from core.config import settings
from aiogram.fsm.context import FSMContext

from core.contracts.api.requests import ConversationRequest
from core.contracts.api.responses import ConversationResponse
from core.contracts.shared import IncomingMessage

rt = Router()

@rt.message()
async def proceed_message(message: Message, state: FSMContext):
    await state.update_data(user_input=message.text)
    request = ConversationRequest(
            telegram_user_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            language_code=message.from_user.language_code,
            message=IncomingMessage(
                message_id=message.message_id,
                sent_at=message.date,
                text=message.text
                ),
    )
    async with httpx.AsyncClient(base_url=settings.api.url) as client:
        response = await client.post(
            "/conversation",
            json=request.model_dump(mode="json"),
        )
        response = ConversationResponse.model_validate(response.json())
    await message.answer(response.text)

# add help command
    