from pydantic import BaseModel
from typing import Optional,Annotated
from fastapi import Form


class CreatePlan(BaseModel):
    name: Annotated[str, Form()]
    gener: Annotated[str, Form()]
    level: Annotated[str, Form()]
    work_out_type: Annotated[str, Form()]
    required_time: Annotated[int, Form()]
    plan_session_type: Annotated[str, Form()]
    sessions: Annotated[str, Form()]

class UpdatePlan(BaseModel):
    name: Optional[str] = None
    gener: Optional[str] = None
    level: Optional[str] = None
    work_out_type: Optional[str] = None
    required_time: Optional[int] = None
    plan_session_type: Optional[str] = None
    sessions: Optional[str] = None


class RemovePlan(BaseModel):
    id:int