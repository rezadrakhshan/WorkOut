from pydantic import BaseModel


class SendEmail(BaseModel):
    to_email : str
