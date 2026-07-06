from infrastructure.db.repositories import UserRepository
from core.contracts.identity import ResolveIdentityRequest, ResolvedIdentity

class IdentityService:
    def __init__(self,
                 user_repository: UserRepository
                 ):
        self.user_repository = user_repository
    
    
    def resolve(self, data: ResolveIdentityRequest) -> ResolvedIdentity:
        pass