from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Alertify'
    description: str = 'Написать микросервис уведомления пользователей'
    model_config = SettingsConfigDict(env_file='.env')

    PORT: int
    EMAIL: str
    DB_URI: str
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_LOGIN: str
    SMTP_PASSWORD: str
    SMTP_EMAIL: str
    SMTP_NAME: str


settings = Settings()
