from core.contracts.conversation import ConversationPipelineIn, ConversationPipelineOut
from infrastructure.db.repositories import UserRepository


class ConversationPipeline:
    def __init__(
            self,
            user_repository: UserRepository,                 
        ):
        self.user_repository = user_repository
    
    async def run(self, data: ConversationPipelineIn) -> ConversationPipelineOut:
        return ConversationPipelineOut(response_text="Привет!")
