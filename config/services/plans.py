from config.db.models import Plan, Exercise
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
    return {"data": new_plan, "message": "plan created"}


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


async def create_exercise_service(exe, db: Session):
    new_exe = Exercise(
        name=exe.name,
        image=exe.image,
        need_equipment=exe.need_equipment,
        equipment_type=exe.equipment_type,
        muscle=exe.muscle,
        difficulty=exe.difficulty,
        sets=exe.sets,
        number_of_sets=exe.number_of_sets,
        required_time=exe.required_time,
        description=exe.description,
    )
    db.add(new_exe)
    db.commit()
    db.refresh(new_exe)
    return {"data":new_exe,"message":"exercise created"}


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
