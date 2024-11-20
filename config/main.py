from fastapi import FastAPI
from routers import send_code,auth
from db import models
from db.database import engine

app = FastAPI(title="WorkOut")


app.include_router(send_code.router)
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)