from fastapi import APIRouter,HTTPException
from config.services.send_code import send_code_with_email_service
from config.schemas.send_code import SendEmail

router = APIRouter()

@router.post("/send-email/")
def send_email_endpoint(email: SendEmail):
    try:
        code = send_code_with_email_service(email)
        return code
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



