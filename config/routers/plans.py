from fastapi import APIRouter, HTTPException, Depends
from schemas.plans import CreateCategory, RemoveCategory
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Category
from services.plans import create_category_service, remove_category_service

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
