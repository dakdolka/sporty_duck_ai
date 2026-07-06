from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.container import container
from infrastructure.db.session import SessionLocal


async def get_session():

    async with SessionLocal() as session:
        yield session


def get_conversation_orchestrator(
    session: AsyncSession = Depends(get_session),
):

    return container.build_conversation_orchestrator(session)