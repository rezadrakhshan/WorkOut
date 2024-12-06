from pydantic import BaseModel


class CreateCategory(BaseModel):
    title: str


class RemoveCategory(BaseModel):
    id: int


class UpdateCategory(BaseModel):
    id: int
    title: str


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
    id:int