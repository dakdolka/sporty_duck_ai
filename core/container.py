# core/container.py

from app.orchestrators import ConversationOrchestrator
from app.pipelines import ConversationPipeline
from infrastructure.db.repositories import UserRepository
from app.services import IdentityService

class Container:

    def __init__(self):
        pass

    def build_conversation_orchestrator(self, session):
        user_repository = UserRepository(session)

        identity_service = IdentityService(
            user_repository=user_repository,
        )

        conversation_pipeline = ConversationPipeline(
            user_repository=user_repository,
        )

        return ConversationOrchestrator(
            identity_service=identity_service,
            conversation_pipeline=conversation_pipeline,
        )


container = Container()