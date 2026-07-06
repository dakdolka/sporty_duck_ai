from app.pipelines import ConversationPipeline
from app.services import IdentityService
from infrastructure.db.repositories import UserRepository

from core.contracts.conversation import ConversationPipelineIn, ConversationPipelineOut, ConversationOrchestratorRequest, ConversationOrchestratorResponse
from core.contracts.identity import ResolveIdentityRequest, ResolvedIdentity


class ConversationOrchestrator:
    def __init__(self,
                 conversation_pipeline: ConversationPipeline,
                 identity_service: IdentityService
            ):
        self.conversation_pipeline = conversation_pipeline
        self.identity_service = identity_service
        
    async def proceed_message(self, request: ConversationOrchestratorRequest):
        identity_data = ResolveIdentityRequest(
            telegram_user_id=request.telegram_user_id,
            username=request.username,
            first_name=request.first_name,
            last_name=request.last_name,
            language_code=request.language_code
            )
        user: ResolvedIdentity = await self.identity_service.resolve(identity_data)
        data = ConversationPipelineIn(
            user_id=user.user_id,
            first_name=user.first_name,
            message=request.message
        )
        result= await self.conversation_pipeline.run(data)
        return ConversationOrchestratorResponse(text=result.response_text)
        
        
            
    