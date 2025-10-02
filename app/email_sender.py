import asyncio
from email.message import EmailMessage

import aiosmtplib

from app.config import Config


async def send_email(to_email: str, subject: str, body: str):
    message = EmailMessage()
    message["From"] = Config.SMTP_USER
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    await aiosmtplib.send(
        message,
        hostname=Config.SMTP_HOST,
        port=Config.SMTP_PORT,
        start_tls=True,
        username=Config.SMTP_USER,
        password=Config.SMTP_PASSWORD,
    )


async def send_bulk_emails(emails: list[str], subject: str, body: str):
    tasks = [send_email(email, subject, body) for email in emails]
    await asyncio.gather(*tasks)
