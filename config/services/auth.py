from fastapi import HTTPException
from db.models import User
from utils.hash_password import hash_password, verify_password, create_access_token


def get_user_information(user, db):
    user_query = db.query(User).filter(User.email == user.email).first()
    if user_query is None:
        raise HTTPException(status_code=404, detail="User does not exists")
    else:
        return user_query


def sign_up_user_service(user, db):
    user_query = db.query(User).filter(User.email == user.email).first()
    if user_query is None:
        new_user = User(email=user.email, password=hash_password(user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User registered successfully"}
    else:
        raise HTTPException(status_code=400, detail="Email already exists")


def sign_in_user_service(user, db):
    user_query = db.query(User).filter(User.email == user.email).first()
    if user_query and verify_password(user.password, user_query.password):
        token = create_access_token(data={"sub": user_query.email})
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=404, detail="Email or password is invalid")
