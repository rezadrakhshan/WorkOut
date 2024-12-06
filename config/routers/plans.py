from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from schemas.plans import *
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Category
from services.plans import *

router = APIRouter(tags=["plans"])


@router.get("/get-category")
def get_category(db: Session = Depends(get_db)):
    try:
        categories = db.query(Category).all()
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-category", response_model=dict)
def create_category_router(category: CreateCategory, db: Session = Depends(get_db)):
    try:
        object = create_category_service(category, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/remove-category", response_model=dict)
def remove_category_router(category: RemoveCategory, db: Session = Depends(get_db)):
    try:
        object = remove_category_service(category, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/update-category", response_model=dict)
def update_category_router(category: UpdateCategory, db: Session = Depends(get_db)):
    try:
        object = update_category_service(category, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
