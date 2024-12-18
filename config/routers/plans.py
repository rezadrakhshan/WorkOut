from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from config.schemas.plans import *
from sqlalchemy.orm import Session
from config.db.database import get_db
from config.db.models import *
from config.services.plans import *
from typing import List

router = APIRouter(tags=["plans"])



@router.post("/create-plan")
async def create_plan_router(
    plan: CreatePlan = Depends(),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:
        object = await create_plan_service(plan, file, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-workout")
async def create_workout_router(
    workout: CreateWorkOut = Depends(),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:
        object = await create_workout_service(workout, file, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/remove-plan")
async def remove_plan_router(plan: RemovePlan, db: Session = Depends(get_db)):
    try:
        object = await remove_plan_service(plan, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/remove-workout")
async def remove_workout_router(workout: RemoveWorkOut, db: Session = Depends(get_db)):
    try:
        object = await remove_workout_service(workout, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/all-plans", response_model=List[PlanResponse])
def get_all_plans(db: Session = Depends(get_db)):
    try:
        plans = db.query(Plan).all()
        return plans
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/single-plan/{plan_id}", response_model=PlanResponse)
def get_single_plan(plan_id: int, db: Session = Depends(get_db)):
    try:
        plan = db.query(Plan).filter(Plan.id == plan_id).first()
        if plan is None:
            raise HTTPException(status_code=404, detail="Plan does not exists")
        return plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/all-workouts")
def get_all_workouts(db: Session = Depends(get_db)):
    try:
        workouts = db.query(WorkOut).all()
        return workouts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/single-workout/{id}")
def get_single_workout(id: int, db: Session = Depends(get_db)):
    try:
        workout = db.query(WorkOut).filter(WorkOut.id == id).first()
        if workout is None:
            raise HTTPException(status_code=404, detail="Workout does not exists")
        return workout
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
