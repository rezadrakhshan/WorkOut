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
    time: str


class CreateWorkOut(BaseModel):
    title: str
    set: int
    type: str
    description: str
    plan: int
