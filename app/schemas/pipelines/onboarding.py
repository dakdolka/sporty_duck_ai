from pydantic import BaseModel

from app.schemas.common import EventInfo, UserInfo

class OnboardingPipelineIn(BaseModel):
    user: UserInfo
    event: EventInfo

class OnboardingPipelineOut(BaseModel):
    message: str