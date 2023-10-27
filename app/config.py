from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    PORT: int  # uvicorn по дефолту запускает на 8000 порту, не будем ничего менять  # noqa
    EMAIL: str # тестовый емейл на который отправляется сообщение взят у тг бота Senthy Email https://t.me/SenthyBot # noqa
    DB_URI: str
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_LOGIN: str
    SMTP_PASSWORD: str
    SMTP_EMAIL: str
    SMTP_NAME: str


settings = Settings()

# from fastapi import FastAPI
# from starlette.responses import JSONResponse
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
# from pydantic import EmailStr, BaseModel
# from typing import List

# class EmailSchema(BaseModel):
#     email: List[EmailStr]


# conf = ConnectionConfig(
#     MAIL_USERNAME = "username",
#     MAIL_PASSWORD = "**********",
#     MAIL_FROM = "test@email.com",
#     MAIL_PORT = 587,
#     MAIL_SERVER = "mail server",
#     MAIL_FROM_NAME="Desired Name",
#     MAIL_STARTTLS = True,
#     MAIL_SSL_TLS = False,
#     USE_CREDENTIALS = True,
#     VALIDATE_CERTS = True
# )

# app = FastAPI()



# @app.post("/email")
# async def simple_send(email: EmailSchema) -> JSONResponse:
#     html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """

#     message = MessageSchema(
#         subject="Fastapi-Mail module",
#         recipients=email.dict().get("email"),
#         body=html,
#         subtype=MessageType.html)

#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return JSONResponse(status_code=200, content={"message": "email has been sent"})
