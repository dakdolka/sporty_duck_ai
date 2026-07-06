from fastapi import APIRouter, Depends

from core.contracts.api.requests import ConversationRequest
from core.contracts.api.responses import ConversationResponse
from app.orchestrators import ConversationOrchestrator

from core.provider import get_conversation_orchestrator
from core.contracts.conversation import ConversationOrchestratorRequest

router = APIRouter(prefix="/conversation", tags=["Conversation"])


@router.post("", response_model=ConversationResponse)
async def conversation(request: ConversationRequest, 
                       orch: ConversationOrchestrator = Depends(get_conversation_orchestrator)
                       ):
    orch_request = ConversationOrchestratorRequest(**request.model_dump(mode="json"))
    return await orch.proceed_message(orch_request)