from app.pipelines import ConversationPipeline
from core.contracts.api import ConversationRequest, ConversationResponse
from infrastructure.db.repositories import UserRepository
from core.contracts.pipelines import ConversationPipelineIn, ConversationPipelineOut


class ConversationService:
    def __init__(self,
                 conversation_pipeline: ConversationPipeline,
                 user_repository: UserRepository
            ):
        self.conversation_pipeline = conversation_pipeline
        self.user_repository = user_repository
        
    async def proceed_message(self, request: ConversationRequest):
        # user = await self.user_repository.require(data_raw.user.id)
        user = request.user
        data = ConversationPipelineIn(user=user, event=request.event)
        result = await self.conversation_pipeline.run(data)
        return ConversationResponse(message=result.llm_answer)
        
        
            
    