from pydantic import BaseModel
from typing import List



class CreatePlan(BaseModel):
    title: str
    time: int


class CreateWorkOut(BaseModel):
    title: str
    set: int
    type: str
    description: str
    plan: int


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
