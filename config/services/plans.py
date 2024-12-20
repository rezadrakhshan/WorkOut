from config.db.models import Plan, Exercise
from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile
import uuid
import aiofiles
from config.schemas.plans import CreateExercise


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


async def create_exercise_service(
    exercise: CreateExercise, file: UploadFile, db: Session
):
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    async with aiofiles.open(f"config/uploaded_files/exercise/{filename}", "wb") as f:
        content = await file.read()
        await f.write(content)

    new_exercise = Exercise(
        name=exercise.name,
        image=f"config/uploaded_files/exercise/{filename}",
        need_equipment=exercise.need_equipment,
        muscle=exercise.muscle,
        difficulty=exercise.difficulty,
        sets=exercise.sets,
        number_of_sets=exercise.number_of_sets,
        required_time=exercise.required_time,
        description=exercise.description,
    )

    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)
    return {"msg": new_exercise}


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

