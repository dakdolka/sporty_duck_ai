from typing import Any, Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

ModelT = TypeVar("ModelT")


class BaseRepository(Generic[ModelT]):
    model: type[ModelT]

    def __init__(self, session: AsyncSession):
        self.session = session

    @staticmethod
    def _build_filters(model: type[ModelT], **filters: Any):
        return [
            getattr(model, field) == value
            for field, value in filters.items()
        ]

    async def create(self, data: BaseModel) -> ModelT:
        instance = self.model(**data.model_dump(mode="json"))

        self.session.add(instance)
        await self.session.flush()

        return instance

    async def get(self, **filters: Any) -> ModelT | None:
        stmt = (
            select(self.model)
            .where(*self._build_filters(self.model, **filters))
        )

        return await self.session.scalar(stmt)

    async def get_many(self, **filters: Any) -> list[ModelT]:
        stmt = (
            select(self.model)
            .where(*self._build_filters(self.model, **filters))
        )

        result = await self.session.scalars(stmt)
        return list(result)

    async def exists(self, **filters: Any) -> bool:
        stmt = (
            select(self.model)
            .where(*self._build_filters(self.model, **filters))
            .limit(1)
        )

        return (await self.session.scalar(stmt)) is not None

    async def update(self, values: dict[str, Any], **filters: Any) -> int:
        stmt = (
            update(self.model)
            .where(*self._build_filters(self.model, **filters))
            .values(**values)
        )

        result = await self.session.execute(stmt)
        return result.rowcount

    async def delete(self, **filters: Any) -> int:
        stmt = (
            delete(self.model)
            .where(*self._build_filters(self.model, **filters))
        )

        result = await self.session.execute(stmt)
        return result.rowcount