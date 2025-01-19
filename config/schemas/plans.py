from pydantic import BaseModel
from typing import Optional


class CreatePlan(BaseModel):
    name: str
    gener: str
    level: str
    work_out_type: str
    required_time: int
    plan_session_type: str
    image:str
    sessions: list = []


class RemovePlan(BaseModel):
    id: int


class CreateExercise(BaseModel):
    name: str
    need_equipment: bool
    muscle: str
    difficulty: str
    sets: list = []
    number_of_sets: int
    required_time: int
    description: str


class GetAllPlans(BaseModel):
    type: Optional[str]
