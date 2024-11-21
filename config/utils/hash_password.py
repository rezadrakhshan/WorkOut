import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    secretkey = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM")
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, secretkey, algorithm=algorithm)
    return encoded_jwt
