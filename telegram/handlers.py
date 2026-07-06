from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
import httpx
from aiogram.fsm.state import State, StatesGroup

from core.contracts.api import EntryResponse, EntryRequest, ConversationRequest, ConversationResponse
from core.contracts.common import EventInfo, UserInfo
from core.config import settings
from aiogram.fsm.context import FSMContext

rt = Router()

class Data(StatesGroup):
    user_input = State()

@rt.message(CommandStart())
async def start(message: Message, state: FSMContext):
    request = EntryRequest(
        user=UserInfo(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                language_code=message.from_user.language_code,
            ),
        event=EventInfo(
                chat_id=str(message.chat.id),
                message_id=str(message.message_id),
                sent_at=message.date,
                text=message.text
        )
        )
    async with httpx.AsyncClient(base_url=settings.api.url) as client:
        response = await client.post(
            "/entry",
            json=request.model_dump(mode="json"),
        )
        response = EntryResponse.model_validate(response.json())
    await message.answer(response.message)
    await state.set_state(Data.user_input)


@rt.message(Data.user_input)
async def proceed_message(message: Message, state: FSMContext):
    await state.update_data(user_input=message.text)
    request = ConversationRequest(
        user=UserInfo(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                language_code=message.from_user.language_code,
            ),
        event=EventInfo(
                chat_id=str(message.chat.id),
                message_id=str(message.message_id),
                sent_at=message.date,
                text=message.text
        )
    )
    async with httpx.AsyncClient(base_url=settings.api.url) as client:
        response = await client.post(
            "/conversation",
            json=request.model_dump(mode="json"),
        )
        response = ConversationResponse.model_validate(response.json())
    await message.answer(response.message)
    await state.set_state(Data.user_input)

# add help command
    