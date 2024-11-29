from pydantic import BaseModel


class CreateCategory(BaseModel):
    title: str


class RemoveCategory(BaseModel):
    id : int