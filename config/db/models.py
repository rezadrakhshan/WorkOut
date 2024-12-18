from config.db.database import Base
from sqlalchemy.types import String, Integer, Boolean, PickleType
from sqlalchemy import Column


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
    name = Column(String)
    gener = Column(String)
    image = Column(String)
    level = Column(String)
    work_out_type = Column(String)
    required_time = Column(Integer)
    plan_session_type = Column(String)
    sessions = Column(PickleType)


class Exercize(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    image = Column(String)
    need_equipment = Column(Boolean, default=False)
    muscle = Column(String)
    difficulty = Column(String)
    number_of_sets = Column(Integer)
    required_time = Column(Integer)
    description = Column(PickleType)
