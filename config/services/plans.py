from config.db.models import Plan, Exercise
from sqlalchemy.orm import Session
from fastapi import HTTPException



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



async def remove_exercise_service(id, db: Session):
    query_object = db.query(Exercise).filter(Exercise.id == id).first()
    if query_object is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    db.delete(query_object)
    db.commit()
    return {"msg": "Exercise deleted"}


async def get_all_plan_service(type, db: Session):
    if type.type != "string":
        db_query = db.query(Plan).filter(Plan.work_out_type == type.type).all()
        return db_query
    db_query = db.query(Plan).all()
    return db_query
