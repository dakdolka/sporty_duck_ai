from fastapi import APIRouter, Depends

from core.contracts.api import ConversationRequest, ConversationResponse
from app.services import ConversationService
from core.provider import get_conversation_service

router = APIRouter(prefix="/conversation", tags=["Conversation"])


@router.post("", response_model=ConversationResponse)
async def conversation(request: ConversationRequest, service: ConversationService = Depends(get_conversation_service)):
    return await service.proceed_message(request)