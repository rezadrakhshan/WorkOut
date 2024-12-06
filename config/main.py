from fastapi import FastAPI
from config.routers import send_code, auth, plans
from config.db import models
from config.db.database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="WorkOut")
app.mount("/config/uploaded_files", StaticFiles(directory="config/uploaded_files"), name="uploaded_files")


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


