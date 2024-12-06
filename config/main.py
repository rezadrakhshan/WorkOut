from fastapi import FastAPI
from config.routers import send_code, auth, plans
from config.db import models
from config.db.database import engine

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


# class ImageMetaData(BaseModel):
#     title: str
#     description: str


# @app.post("/upload/")
# async def upload_image(
#     metadata: ImageMetaData = Depends(),
#     file: UploadFile = File(...)
# ):
#     filename = file.filename

#     # ذخیره فایل
#     with open(f"uploaded_files/{filename}", "wb") as f:
#         content = await file.read()
#         f.write(content)

#     return {
#         "title": metadata.title,
#         "description": metadata.description,
#         "filename": filename
#     }
