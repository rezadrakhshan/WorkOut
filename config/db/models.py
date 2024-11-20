from db.database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

