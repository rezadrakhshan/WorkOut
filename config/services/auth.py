from fastapi import HTTPException
from sqlalchemy.orm import Session
from config.db.models import User, Profile
import jwt
from config.utils.hash_password import (
    hash_password,
    verify_password,
    create_access_token,
)
from dotenv import load_dotenv
from pathlib import Path
import os
import uuid

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.getenv("SECRET_KEY")


def get_current_user(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(decoded_token)
        return decoded_token
    except jwt.ExpiredSignatureError:
        print("Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")


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
        token = create_access_token(data={"sub": str(new_user.id)})
        profile = Profile(  
            user_id=new_user.id,
            image="config/uploaded_files/User/default.jpg",
        )
        db.add(profile)
        db.commit()
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Email already exists")


def sign_in_user_service(user, db):
    user_query = db.query(User).filter(User.email == user.email).first()
    if user_query and verify_password(user.password, user_query.password):
        token = create_access_token(data={"sub": str(user_query.id)})
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=404, detail="Email or password is invalid")


def change_password_service(user, db):
    user_query = db.query(User).filter(User.email == user.email).first()
    if user_query:
        new_password = hash_password(user.new_password)
        user_query.password = new_password
        db.commit()
        db.refresh(user_query)
        return {"message": "Password changed successfully"}
    else:
        raise HTTPException(status_code=404, detail="Email is invalid")


async def update_profile_service(data, db: Session):
    user = get_current_user(data["token"])
    if user is None:
        raise ValueError("Invalid or expired token")
    get_user = db.query(User).filter(User.id == int(user["sub"])).first()
    get_profile = db.query(Profile).filter(Profile.user_id == get_user.id).first()
    print(3)
    if data["name"] != "string" and data["name"] != "":
        get_profile.name = data["name"]
    if data["user_name"] != "string" and data["user_name"] != "":
        get_profile.user_name = data["user_name"]
    if data["email"] != "string" and data["email"] != "":
        get_profile.email = data["email"]
    if data["image"] != "no.txt" and data["image"] != "":
        filename = f"{uuid.uuid4().hex}_{data['image'].filename}"
        if get_profile.image == "config/uploaded_files/User/default.jpg":
            with open(f"config/uploaded_files/User/{filename}", "wb") as f:
                content = await data["image"].read()
                f.write(content)
            get_profile.image = f"config/uploaded_files/User/{filename}"
        else:
            os.remove(get_profile.image)
            with open(f"config/uploaded_files/User/{filename}", "wb") as f:
                content = await data["image"].read()
                f.write(content)
            get_profile.image = f"config/uploaded_files/User/{filename}"
            get_profile.image = f"config/uploaded_files/User/{filename}"
    db.commit()
    return {"msg": "ok"}
