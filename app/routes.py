from fastapi import APIRouter

from app.email_sender import send_email, send_bulk_emails
from app.models import PromotionalEmailRequest, ConfirmEmailRequest, ResetPasswordRequest


router = APIRouter()


@router.post("/api/newsletter")
async def send_promotional_email(data: PromotionalEmailRequest):
    await send_bulk_emails(data.emails, data.title, data.content)
    return {"message": f"Promotional emails sent to {len(data.emails)} customers"}


@router.post("/api/email-confirmation")
async def send_confirmation_email(data: ConfirmEmailRequest):
    subject = "Pizza Delicious - Confirm Your Email"
    body = f"Click the link to confirm your email: {data.confirm_link}."
    await send_email(data.email, subject, body)
    return {"message": f"Confirmation email sent to {data.email}"}


@router.post("/api/password-reset")
async def send_reset_email(data: ResetPasswordRequest):
    subject = "Pizza Delicious - Reset Your Password"
    body = f"Click the link to reset your password: {data.reset_link}."
    await send_email(data.email, subject, body)
    return {"message": f"Password reset email sent to {data.email}"}