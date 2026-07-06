from core.contracts.repositories import CreateUserRequest, UpdateUserRequest
from infrastructure.db.repositories import UserRepository
from core.contracts.identity import ResolveIdentityRequest, ResolvedIdentity

class IdentityService:
    def __init__(self,
                 user_repository: UserRepository
                 ):
        self.user_repository = user_repository
    
    
    async def resolve(
        self,
        data: ResolveIdentityRequest,
    ) -> ResolvedIdentity:

        user = await self.user_repository.get_by_telegram_id(
            data.telegram_user_id,
        )

        created = False

        if user is None:
            user = await self.user_repository.create(
                CreateUserRequest(
                    telegram_user_id=data.telegram_user_id,
                    username=data.username,
                    first_name=data.first_name,
                    last_name=data.last_name,
                    language_code=data.language_code,
                )
            )

            created = True

        else:
            if (
                user.username != data.username
                or user.first_name != data.first_name
                or user.last_name != data.last_name
                or user.language_code != data.language_code
            ):
                user = await self.user_repository.update(
                    UpdateUserRequest(
                        user_id=user.id,
                        username=data.username,
                        first_name=data.first_name,
                        last_name=data.last_name,
                        language_code=data.language_code,
                    )
                )

        return ResolvedIdentity(
            user_id=user.id,
            first_name=user.first_name,
            is_new=created,
        )