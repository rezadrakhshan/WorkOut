from pydantic import BaseModel
from typing import List



class CreatePlan(BaseModel):
    name:str
    gener:str
    image:str
    level:str
    work_out_type:str
    required_time:int
    plan_session_type:str
    sessions:str




class CreateWorkOut(BaseModel):
    title: str
    set: int
    type: str
    description: str
    plan_id: int


class RemovePlan(BaseModel):
    id: int


class RemoveWorkOut(BaseModel):
    id: int


class PlanResponse(BaseModel):
    id: int
    title: str
    time: str
    image: str
    workouts: List["WorkOutResponse"] = []


class WorkOutResponse(BaseModel):
    id: int
    title: str
    set: int
    image: str
    type: str
    description: str
    plan_id: int

    class Config:
        orm_mode = True
