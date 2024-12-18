from pydantic import BaseModel
from typing import Optional


class CreatePlan(BaseModel):
    name: str
    gener: str
    image: str
    level: str
    work_out_type: str
    required_time: int
    plan_session_type: str
    sessions: str


class UpdatePlan(BaseModel):
    id: int
    name: Optional[str] = None
    gener: Optional[str] = None
    image: Optional[str] = None
    level: Optional[str] = None
    work_out_type: Optional[str] = None
    required_time: Optional[int] = None
    plan_session_type: Optional[str] = None
    sessions: Optional[str] = None


class RemovePlan(BaseModel):
    id:int