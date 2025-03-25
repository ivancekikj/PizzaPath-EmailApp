import asyncio
from email.message import EmailMessage
from aiosmtplib import SMTP
from app.config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD


async def send_email(to_email: str, subject: str, body: str):
    message = EmailMessage()
    message["From"] = SMTP_USER
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    async with SMTP(hostname=SMTP_HOST, port=SMTP_PORT, start_tls=True) as smtp:
        await smtp.connect()
        await smtp.login(SMTP_USER, SMTP_PASSWORD)
        await smtp.send_message(message)


async def send_bulk_emails(emails: list[str], subject: str, body: str):
    tasks = [send_email(email, subject, body) for email in emails]
    await asyncio.gather(*tasks)