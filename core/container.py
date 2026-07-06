
from app.pipelines import ConversationPipeline
from app.orchestrators import ConversationOrchestrator
from app.services import IdentityService
from infrastructure.db.repositories import UserRepository



class Container:
    def __init__(self):
        
        
        
        # ====repositories==== #
        self.user_repository = UserRepository()

        # ====piplines==== #
        self.conversation_pipeline = ConversationPipeline(
            self.user_repository
        )

        # ====services==== #
        
        self.identity_service = IdentityService(
            self.user_repository
        )
        
        # ====orchestrators==== #
        self.conversation_orchestrator = ConversationOrchestrator(
            self.conversation_pipeline,
            self.user_repository
        )
    
container = Container()