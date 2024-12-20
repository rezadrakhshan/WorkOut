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
    sessions: Annotated[str, Form()],
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
    db: Session = Depends(get_db),
):
    plan = CreatePlan(
        name=name,
        gener=gener,
        level=level,
        work_out_type=work_out_type,
        required_time=required_time,
        plan_session_type=plan_session_type,
        sessions=sessions,
    )
    try:
        object = await create_plan_service(plan, file, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/remove-plan")
async def remove_plan_router(id: RemovePlan, db: Session = Depends(get_db)):
    try:
        object = await remove_plan_service(id, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get-all-plan")
async def get_all_plan_router(db: Session = Depends(get_db)):
    try:
        plan_query = db.query(Plan).all()
        return plan_query
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
    image: Annotated[UploadFile, File(description="A file read as UploadFile")],
    need_equipment: Annotated[bool, Form()],
    muscle: Annotated[str, Form()],
    difficulty: Annotated[str, Form()],
    sets: Annotated[List[int], Form()],
    number_of_sets: Annotated[int, Form()],
    required_time: Annotated[int, Form()],
    description: Annotated[str, Form()],
    db: Session = Depends(get_db),
):
    exercise = CreateExercise(
        name=name,
        need_equipment=need_equipment,
        muscle=muscle,
        difficulty=difficulty,
        sets=sets,
        number_of_sets=number_of_sets,
        required_time=required_time,
        description=description,
    )
    try:
        object = await create_exercise_service(exercise, image, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/remove-exercise/{exercise_id}")
async def remove_exercise_router(exercise_id: int, db: Session = Depends(get_db)):
    try:
        object = await remove_exercise_service(exercise_id, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
