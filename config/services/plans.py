from config.db.models import Plan
from fastapi import HTTPException
import uuid
from sqlalchemy.orm import Session


async def create_plan_service(plan, db: Session):
    new_plan = Plan(
        name=plan.name,
        gener=plan.gener,
        image=plan.image,
        level=plan.level,
        work_out_type=plan.work_out_type,
        required_time=plan.required_time,
        plan_session_type=plan.plan_session_type,
        sessions=plan.sessions,
    )
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return {"msg": new_plan}

