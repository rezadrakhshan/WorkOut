from config.db.models import Plan
from config.schemas.plans import UpdatePlan
from sqlalchemy.orm import Session
from fastapi import HTTPException,UploadFile
import uuid


async def create_plan_service(plan, file, db: Session):
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    with open(f"config/uploaded_files/Plan/{filename}", "wb") as f:
        content = await file.read()
        f.write(content)
    new_plan = Plan(
        name=plan.name,
        gener=plan.gener,
        image=f"config/uploaded_files/Plan/{filename}",
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

async def update_plan_service(plan_id: int, plan: UpdatePlan, file: UploadFile, db: Session):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()

    if not db_plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    if file:
        filename = f"{uuid.uuid4().hex}_{file.filename}"
        with open(f"config/uploaded_files/Plan/{filename}", "wb") as f:
            content = await file.read()
            f.write(content)
        db_plan.image = f"config/uploaded_files/Plan/{filename}"

    if plan.name is not None:
        db_plan.name = plan.name
    if plan.gener is not None:
        db_plan.gener = plan.gener
    if plan.level is not None:
        db_plan.level = plan.level
    if plan.work_out_type is not None:
        db_plan.work_out_type = plan.work_out_type
    if plan.required_time is not None:
        db_plan.required_time = plan.required_time
    if plan.plan_session_type is not None:
        db_plan.plan_session_type = plan.plan_session_type
    if plan.sessions is not None:
        db_plan.sessions = plan.sessions

    db.commit()
    db.refresh(db_plan)
    return {"msg": db_plan}



async def remove_plan_service(plan_id, db: Session):
    db_query = db.query(Plan).filter(Plan.id == plan_id.id).first()
    if db_query is None:
        raise HTTPException(status_code=404, detail="Plan does not exists")
    db.delete(db_query)
    db.commit()
    return {"msg": "Plans deleted"}


async def get_single_plan_service(plan_id, db: Session):
    db_query = db.query(Plan).filter(Plan.id == plan_id).first()
    if db_query is None:
        raise HTTPException(status_code=404, detail="Plan does not exists")
    return db_query
