from config.db.models import Plan
from sqlalchemy.orm import Session
from fastapi import HTTPException


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


async def update_plan_service(plan, db: Session):
    db_query = db.query(Plan).filter(Plan.id == plan.id).first()
    if db_query is None:
        raise HTTPException(status_code=404, detail="Plan does not exists")
    db_query.name = plan.name if plan.name != "" else db_query.name
    db_query.gener = plan.gener if plan.gener != "" else db_query.gener
    db_query.image = plan.image if plan.image != "" else db_query.image
    db_query.level = plan.level if plan.level != "" else db_query.level
    db_query.work_out_type = (
        plan.work_out_type if plan.work_out_type != "" else db_query.work_out_type
    )
    db_query.required_time = (
        plan.required_time if plan.required_time != "" else db_query.required_time
    )
    db_query.plan_session_type = (
        plan.plan_session_type
        if plan.plan_session_type != ""
        else db_query.plan_session_type
    )
    db_query.sessions = plan.sessions if plan.sessions != "" else db_query.sessions
    db.commit()
    return {"msg": "Plan updated"}


async def remove_plan_service(plan_id, db: Session):
    db_query = db.query(Plan).filter(Plan.id == plan_id.id).first()
    if db_query is None:
        raise HTTPException(status_code=404, detail="Plan does not exists")
    db.delete(db_query)
    db.commit()
    return {"msg": "Plans deleted"}


async def get_single_plan_service(plan_id,db:Session):
    db_query = db.query(Plan).filter(Plan.id == plan_id).first()
    if db_query is None:
        raise HTTPException(status_code=404,detail="Plan does not exists")
    return db_query
