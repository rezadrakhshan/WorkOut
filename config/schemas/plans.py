from pydantic import BaseModel
from typing import Optional


class RemovePlan(BaseModel):
    id: int



class GetAllPlans(BaseModel):
    type: Optional[str]
