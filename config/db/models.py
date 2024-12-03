from db.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    time = Column(String)
    image = Column(String)
    workout = relationship("Category", back_populates="plan")


class WorkOut(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    set = Column(Integer)
    image = Column(String)
    type = Column(String)
    description = Column(String)
    plan = relationship("Plan", back_populates="workout")
