
from app.pipelines import OnboardingPipeline, ConversationPipeline
from app.services import EntryService, ConversationService
from infrastructure.db.repositories import UserRepository


class Container:
    def __init__(self):
        
        # ====repositories==== #
        self.user_repository = UserRepository()

        # ====piplines==== #
        self.onboarding_pipeline = OnboardingPipeline(
            self.user_repository
        )
        self.conversation_pipeline = ConversationPipeline(
            self.user_repository
        )

        # ====services==== #
        self.entry_service = EntryService(
            self.user_repository,
            self.onboarding_pipeline,
            self.conversation_pipeline,
        )
        
        self.conversation_service = ConversationService(
            self.conversation_pipeline,
            self.user_repository
        )
    
container = Container()