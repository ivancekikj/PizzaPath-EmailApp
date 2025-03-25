import os

from dotenv import load_dotenv


SMTP_HOST = None
SMTP_PORT = None
SMTP_USER = None
SMTP_PASSWORD = None
ADMIN_APP = None


def load_settings():
    global SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, ADMIN_APP
    load_dotenv()

    assert os.getenv("SMTP_HOST") is not None and os.getenv("SMTP_HOST") != "", "SMTP_HOST not configured"
    assert os.getenv("SMTP_PORT") is not None and os.getenv("SMTP_PORT") != "", "SMTP_PORT not configured"
    assert os.getenv("SMTP_USER") is not None and os.getenv("SMTP_USER") != "", "SMTP_USER not configured"
    assert os.getenv("SMTP_PASSWORD") is not None and os.getenv("SMTP_PASSWORD") != "", "SMTP_PASSWORD not configured"
    assert os.getenv("ADMIN_APP") is not None and os.getenv("ADMIN_APP") != "", "ADMIN_APP not configured"

    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    ADMIN_APP = os.getenv("ADMIN_APP")
