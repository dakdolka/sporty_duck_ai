from core.contracts.common import UserInfo

from .base_repository import BaseRepository
from infrastructure.db.models.user import User

class UserRepository(BaseRepository[User]):
    model = User
    