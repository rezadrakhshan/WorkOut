from fastapi import APIRouter, HTTPException, Depends
from schemas.auth import SignUp
from db.database import get_db
from sqlalchemy.orm import Session
from services.auth import sign_up_user_service

router = APIRouter(tags=["Authentication"])


@router.post("/sign_up", response_model=SignUp)
def sign_up_router(user: SignUp, db: Session = Depends(get_db)):
    object = sign_up_user_service(user, db)
    return object
