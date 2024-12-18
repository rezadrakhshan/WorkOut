from fastapi import APIRouter, HTTPException, Depends
from config.schemas.plans import *
from sqlalchemy.orm import Session
from config.db.database import get_db
from config.db.models import *
from config.services.plans import *

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


@router.patch("/update-plan")
async def update_plan_router(plan: UpdatePlan, db: Session = Depends(get_db)):
    try:
        object = await update_plan_service(plan, db)
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
        object = await get_single_plan_service(plan_id,db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
