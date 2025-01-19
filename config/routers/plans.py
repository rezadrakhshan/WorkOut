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
    plan: CreatePlan,
    db: Session = Depends(get_db),
):
    try:
        object = await create_plan_service(plan, db)
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
    exe: CreateExercise,
    db: Session = Depends(get_db),
):
    try:
        object = await create_exercise_service(exe, db)
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
