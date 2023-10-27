import smtplib
from email.message import EmailMessage

# from celery import Celery

from config import settings

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

# celery = Celery('tasks', broker='redis://localhost:6379')

# async def send_email():
#     pass


# email, "Notification", f"You have a new notification: {notification.key}"

def set_email_content(notification: str):
    email = EmailMessage()
    email['Subject'] = 'Notification'
    email['From'] = settings.SMTP_LOGIN
    email['To'] = settings.EMAIL

    email.set_content(
        '<div>'
        f'<h1 style="color: red;"> Вы получили новое уведомление: {notification} </h1>'
        '</div>',
        subtype='html'
    )
    return email


def send_email(notification: str):
    email = set_email_content(notification)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(settings.SMTP_LOGIN, settings.SMTP_PASSWORD)
        server.send_message(email)