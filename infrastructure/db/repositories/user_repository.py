from app.schemas.api.entry import EntryRequest

class UserRepository:

    async def exists(self, user_id: str) -> bool:
        """
        Проверяет существование пользователя.
        """

        return False

    async def create(self, data: EntryRequest):
        """
        Создает пользователя.
        """

        pass
    
    async def require(self, user_id: str) -> EntryRequest:
        """
        Возвращает пользователя или ошибку!
        """

        pass