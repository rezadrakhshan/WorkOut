from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from config.schemas.plans import *
from sqlalchemy.orm import Session
from config.db.database import get_db
from config.db.models import *
from config.services.plans import *
from typing import Annotated

router = APIRouter(tags=["plans"])


@router.post("/create-plan")
async def create_plan_router(
    name: Annotated[str, Form()],
    gener: Annotated[str, Form()],
    level: Annotated[str, Form()],
    work_out_type: Annotated[str, Form()],
    required_time: Annotated[int, Form()],
    plan_session_type: Annotated[str, Form()],
    image: Annotated[UploadFile, File()],
    sessions: Annotated[list, Form()],
    db: Session = Depends(get_db),
):
    try:
        with open(f"config/uploaded_files/Plan/{image.filename}", "wb") as f:
            content = await image.read()
            f.write(content)
        new_plan = Plan(
            name=name,
            gener=gener,
            image=image.filename,
            level=level,
            work_out_type=work_out_type,
            required_time=required_time,
            plan_session_type=plan_session_type,
            sessions=sessions,
        )
        db.add(new_plan)
        db.commit()
        db.refresh(new_plan)
        return new_plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/remove-plan")
async def remove_plan_router(id: RemovePlan, db: Session = Depends(get_db)):
    try:
        object = await remove_plan_service(id, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/get-all-plan")
async def get_all_plan_router(type: GetAllPlans, db: Session = Depends(get_db)):
    try:
        object = await get_all_plan_service(type, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get-single-plan/{plan_id}")
async def get_single_plan_router(plan_id: int, db: Session = Depends(get_db)):
    try:
        object = await get_single_plan_service(plan_id, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-exercise")
async def create_exercise_router(
    name: Annotated[str, Form()],
    need_equipment: Annotated[bool, Form()],
    equipment_type: Annotated[str, Form()],
    image: Annotated[UploadFile, File()],
    muscle: Annotated[str, Form()],
    difficulty: Annotated[str, Form()],
    sets: Annotated[list, Form()],
    number_of_sets: Annotated[int, Form()],
    required_time: Annotated[int, Form()],
    description: Annotated[str, Form()],
    db: Session = Depends(get_db),
):
    try:
        with open(f"config/uploaded_files/exercise/{image.filename}", "wb") as f:
            content = await image.read()
            f.write(content)
        new_exe = Exercise(
            name=name,
            image=image.filename,
            need_equipment=need_equipment,
            equipment_type=equipment_type,
            muscle=muscle,
            difficulty=difficulty,
            sets=sets,
            number_of_sets=number_of_sets,
            required_time=required_time,
            description=description,
        )
        db.add(new_exe)
        db.commit()
        db.refresh(new_exe)
        return new_exe
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/remove-exercise/{exercise_id}")
async def remove_exercise_router(exercise_id: int, db: Session = Depends(get_db)):
    try:
        object = await remove_exercise_service(exercise_id, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get-all-exercise")
async def get_all_exercise_router(db: Session = Depends(get_db)):
    try:
        db_query = db.query(Exercise).all()
        return db_query
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get-single-exercise/{id}")
async def get_single_exercise(id: int, db: Session = Depends(get_db)):
    try:
        db_query = db.query(Exercise).filter(Exercise.id == id).first()
        if db_query is None:
            raise HTTPException(status_code=404, detail="Exercise not found")
        return db_query
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
