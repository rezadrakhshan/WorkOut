from fastapi import APIRouter, HTTPException, Depends
from schemas.plans import CreateCategory
from sqlalchemy.orm import Session
from db.database import get_db
from services.plans import create_category_service

router = APIRouter(tags=["plans"])


@router.post("/create-category", response_model=dict)
def create_category_router(category: CreateCategory, db: Session = Depends(get_db)):
    try:
        object = create_category_service(category, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
