from fastapi import FastAPI
from routers import send_code

app = FastAPI(title="WorkOut")


app.include_router(send_code.router)
