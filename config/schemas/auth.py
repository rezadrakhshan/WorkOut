from pydantic import BaseModel


class SignUp(BaseModel):
    email: str
    password: str


class SignIn(BaseModel):
    email: str
    password: str


class GetUserInformation(BaseModel):
    email: str
