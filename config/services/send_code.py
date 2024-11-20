from fastapi import HTTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import smtplib
from pathlib import Path
import random


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def send_code_with_email_service(email):
    smtp_server = os.getenv("HOST")
    smtp_port = int(os.getenv("PORT"))
    sender_email = os.getenv("EMAIL")
    sender_password = os.getenv("PASSWORD")

    if not all([smtp_server, smtp_port, sender_email, sender_password]):
        raise HTTPException(status_code=500, detail="Email configuration is incomplete")

    code = str(random.randint(1000,9999))
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email.to_email
    msg["Subject"] = "Your Verification Code is Here!"
    msg.attach(MIMEText(code, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

    return {"msg":code}
