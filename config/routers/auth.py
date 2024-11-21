from fastapi import APIRouter, Depends, HTTPException
from schemas.auth import SignUp, SignIn
from db.database import get_db
from sqlalchemy.orm import Session
from services.auth import sign_up_user_service, sign_in_user_service

router = APIRouter(tags=["Authentication"])


@router.post("/sign_up", response_model=dict)
def sign_up_router(user: SignUp, db: Session = Depends(get_db)):
    try:
        object = sign_up_user_service(user, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sign_in", response_model=dict)
def sign_in_router(user: SignIn, db: Session = Depends(get_db)):
    try:
        object = sign_in_user_service(user, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
