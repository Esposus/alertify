import smtplib
from email.message import EmailMessage

from fastapi import HTTPException, status

from config import settings


def set_email_content(notification: str):
    email = EmailMessage()
    email['Subject'] = settings.SMTP_NAME
    email['From'] = settings.SMTP_LOGIN
    email['To'] = settings.EMAIL

    if notification == 'registration':
        email.set_content(
            '<div>'
            '<h3 style="color: red;"> Регистрация прошла успешно </h3>'
            f'статус: {notification}'
            '</div>',
            subtype='html'
        )
    elif notification == 'new_login':
        email.set_content(
            '<div>'
            '<h3 style="color: red;"> Ваш логин обновлен! </h3>'
            f'статус: {notification}'
            '</div>',
            subtype='html'
        )
    return email


def send_email(notification: str):
    try:
        email = set_email_content(notification)
        with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.login(settings.SMTP_LOGIN, settings.SMTP_PASSWORD)
            server.send_message(email)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Ошибка при отправке электронной почты: {str(e)}'
        )
