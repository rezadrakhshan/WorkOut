from fastapi import HTTPException
from db.models import User
from utils.hash_password import hash_password


def sign_up_user_service(user, db):
    user_query = db.query(User).filter(User.email == user.email).first()
    if user_query is None:
        new_user = User(email=user.email, password=hash_password(user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        raise HTTPException(status_code=200,detail="User registered successfully")
    else:
        raise HTTPException(status_code=400, detail="Email already exists")
