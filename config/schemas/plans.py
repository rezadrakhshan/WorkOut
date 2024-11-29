from pydantic import BaseModel


class CreateCategory(BaseModel):
    title: str
