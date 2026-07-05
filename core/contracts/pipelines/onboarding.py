from pydantic import BaseModel

from core.contracts.common import EventInfo, UserInfo

class OnboardingPipelineIn(BaseModel):
    user: UserInfo
    event: EventInfo

class OnboardingPipelineOut(BaseModel):
    message: str