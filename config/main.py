from fastapi import FastAPI,File, Form, UploadFile
from config.routers import send_code, auth, plans
from config.db import models
from config.db.database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

app = FastAPI(title="WorkOut")
app.mount("/config/uploaded_files", StaticFiles(directory="config/uploaded_files"), name="uploaded_files")


@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
): 
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }

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


