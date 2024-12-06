from config.db.models import Category, Plan, WorkOut
from fastapi import HTTPException
import uuid
from sqlalchemy.orm import Session


def create_category_service(category, db):
    new_category = Category(title=category.title)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {"msg": "Category was create"}


def remove_category_service(category, db):
    category_object = db.query(Category).filter(Category.id == category.id).first()
    if category_object is None:
        raise HTTPException(status_code=404, detail="Category does not exists")
    db.delete(category_object)
    db.commit()
    return {"msg": "Category was deleted"}


def update_category_service(category, db):
    object = db.query(Category).filter(Category.id == category.id).first()
    if object is None:
        raise HTTPException(status_code=404, detail="Category does not exists")
    object.title = category.title
    db.commit()
    return {"msg": "Category Updated"}


async def create_plan_service(plan, file, db):
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    with open(f"config/uploaded_files/Plan/{filename}", "wb") as f:
        content = await file.read()
        f.write(content)

    new_plan = Plan(
        title=plan.title, time=plan.time, image=f"config/uploaded_files/Plan/{filename}"
    )
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return {"msg": new_plan}


async def create_workout_service(workout, file, db):
    get_plan = db.query(Plan).filter(Plan.id == workout.plan_id).first()
    if get_plan is None:
        raise HTTPException(status_code=404, detail="Plan does not exists")
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    with open(f"config/uploaded_files/Workout/{filename}", "wb") as f:
        content = await file.read()
        f.write(content)
    new_workout = WorkOut(
        title=workout.title,
        set=workout.set,
        image=f"config/uploaded_files/Workout/{filename}",
        type=workout.type,
        description=workout.description,
        plan_id=workout.plan_id,
    )
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    return new_workout


async def remove_plan_service(plan, db: Session):
    plan = db.query(Plan).filter(Plan.id == plan.id).first()
    if plan is None:
        raise HTTPException(status_code=404, detail="Plan does not exists")
    workouts = db.query(WorkOut).filter(WorkOut.plan_id == plan.id)
    for i in workouts:
        db.delete(i)
        db.commit()
    db.delete(plan)
    db.commit()
    return {"msg": "Plan was delete"}


async def remove_workout_service(workout, db: Session):
    workout = db.query(WorkOut).filter(WorkOut.id == workout.id).first()
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout does not exists")
    db.delete(workout)
    db.commit()
    return {"msg": "Workout was delete"}
