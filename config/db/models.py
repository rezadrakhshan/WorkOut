from config.db.database import Base
from sqlalchemy.types import String, Integer
from sqlalchemy import Column, ForeignKey
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
    workouts = relationship("WorkOut", back_populates="plan")  

class WorkOut(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    set = Column(Integer)
    image = Column(String)
    type = Column(String)
    description = Column(String)
    plan_id = Column(Integer, ForeignKey("plans.id"))
    plan = relationship("Plan", back_populates="workouts")

