from core.contracts.pipelines import OnboardingPipelineIn, OnboardingPipelineOut
from infrastructure.db.repositories import UserRepository


class OnboardingPipeline:
    
    def __init__(
        self,
        user_repository: UserRepository,
    ):
        self.user_repository = user_repository

    async def run(
        self,
        data: OnboardingPipelineIn,
    ) -> OnboardingPipelineOut:

        # TODO:
        # создать память
        # создать conversation
        # вернуть первое сообщение

        return OnboardingPipelineOut(
            message="Привет! Давай познакомимся."
        )