import os

from dotenv import load_dotenv


class Config:
    SMTP_HOST: str = None
    SMTP_PORT: int = None
    SMTP_USER: str = None
    SMTP_PASSWORD: str = None


def load_settings():
    load_dotenv()

    Config.SMTP_HOST = os.getenv("SMTP_HOST")
    Config.SMTP_PORT = int(os.getenv("SMTP_PORT"))
    Config.SMTP_USER = os.getenv("SMTP_USER")
    Config.SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

    assert Config.SMTP_HOST is not None and Config.SMTP_HOST != "", "SMTP_HOST not configured"
    assert Config.SMTP_PORT is not None and Config.SMTP_PORT != "", "SMTP_PORT not configured"
    assert Config.SMTP_USER is not None and Config.SMTP_USER != "", "SMTP_USER not configured"
    assert Config.SMTP_PASSWORD is not None and Config.SMTP_PASSWORD != "", "SMTP_PASSWORD not configured"
