from tkinter import ON

from app.pipelines import OnboardingPipeline, ConversationPipeline
from core.contracts.pipelines import OnboardingPipelineIn, ConversationPipelineIn
from infrastructure.db.repositories import UserRepository
from core.contracts.api import EntryRequest, EntryResponse


class EntryService:

    def __init__(self,
                 user_repository: UserRepository,
                 onboarding_pipeline: OnboardingPipeline,
                 conversation_pipeline: ConversationPipeline
        ):

        self.user_repository = user_repository

        self.onboarding_pipeline = onboarding_pipeline
        self.conversation_pipeline = conversation_pipeline

    async def enter(
        self,
        request: EntryRequest,
    ) -> EntryResponse:
        
        exists = await self.user_repository.exists(
            user_id=request.user.telegram_id,
        )
        
        if not exists:
            data = OnboardingPipelineIn(user=request.user, event=request.event)
            return await self.onboarding_pipeline.run(data)
        data = ConversationPipelineIn(user=request.user, event=request.event)
        return await self.conversation_pipeline.run(data)