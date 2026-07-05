from tkinter import ON

from app.pipelines import OnboardingPipeline, ConversationPipeline
from app.schemas.pipelines import OnboardingPipelineIn
from infrastructure.db.repositories import UserRepository
from app.schemas.api import EntryRequest, EntryResponse


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
            user_id=request.user.id,
        )
        
        data = OnboardingPipelineIn(user=request.user, event=request.event)
        if not exists:
            return await self.onboarding_pipeline.run(data)
        return await self.conversation_pipeline.run(data)