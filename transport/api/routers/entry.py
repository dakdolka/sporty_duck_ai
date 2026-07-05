from fastapi import APIRouter, Depends

from core.contracts.api import EntryRequest, EntryResponse
from app.services import EntryService
from core.provider import get_entry_service

router = APIRouter(prefix="/entry", tags=["Entry"])


@router.post("", response_model=EntryResponse)
async def entry(request: EntryRequest,
                service: EntryService = Depends(get_entry_service)):
    return await service.enter(request)