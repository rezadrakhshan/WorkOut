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
    plan: CreatePlan,
    db: Session = Depends(get_db),
):
    try:
        object = await create_plan_service(plan, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


