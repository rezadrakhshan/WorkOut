from pydantic import BaseModel,EmailStr
from typing import Optional


class SignUp(BaseModel):
    email: str
    password: str


class SignIn(BaseModel):
    email: str
    password: str


class GetUserInformation(BaseModel):
    email: str


class ChangePassword(BaseModel):
    email: str
    new_password: str


class UpdateProfileRequest(BaseModel):
    name: Optional[str] = None
    user_name: Optional[str] = None
    image: Optional[str] = None