from .base_repository import BaseRepository
from infrastructure.db.models.user import User
from core.contracts.repositories import UserRecord

class UserRepository(BaseRepository[User]):
    model = User
    
    async def get_by_telegram_id(self, telegram_user_id: int) -> UserRecord  | None:
        user =  await self.get(telegram_user_id=telegram_user_id)
        if user is None:
            return None
        result = UserRecord(
            id=user.id,
            telegram_user_id=user.telegram_user_id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            language_code=user.language_code,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
        return result
    