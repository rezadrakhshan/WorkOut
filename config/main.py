from fastapi import FastAPI
from routers import send_code, auth, plans
from db import models
from db.database import engine

app = FastAPI(title="WorkOut")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(send_code.router)
app.include_router(auth.router)
app.include_router(plans.router)

models.Base.metadata.create_all(bind=engine)
