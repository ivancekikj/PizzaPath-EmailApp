from typing import List

from pydantic import BaseModel, EmailStr


class PromotionalEmailRequest(BaseModel):
    emails: List[EmailStr]
    title: str
    content: str


class ConfirmEmailRequest(BaseModel):
    email: EmailStr
    confirm_link: str


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    reset_link: str
