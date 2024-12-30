from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, File
from config.schemas.auth import *
from config.schemas.send_code import SendEmail
from config.services.send_code import send_code_with_email_service
from config.db.database import get_db
from sqlalchemy.orm import Session
from config.services.auth import *
from config.db.models import User
from typing import Dict

router = APIRouter(tags=["Authentication"])


@router.post("/get_user_information")
def get_user_information_router(
    user: GetUserInformation, db: Session = Depends(get_db)
):
    try:
        object = get_user_information(user, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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


@router.post("/send_code_for_change_password", response_model=dict)
def send_code_for_change_password(email: SendEmail, db: Session = Depends(get_db)):
    try:
        user_query = db.query(User).filter(User.email == email.to_email).first()
        if user_query is None:
            raise HTTPException(status_code=404, detail="User does not exist")
        else:
            object = send_code_with_email_service(email)
            return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/change_password", response_model=dict)
def change_password_router(user: ChangePassword, db: Session = Depends(get_db)):
    try:
        object = change_password_service(user, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/update-profile")
async def update_profile_router(
    token=Form(),
    name=Form(None),
    user_name=Form(None),
    email=Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db),
):
    try:
        data = {
            "token": token,
            "name": name,
            "user_name": user_name,
            "email": email,
            "image": image,
        }
        object = await update_profile_service(data, db)
        return object
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
