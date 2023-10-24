from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    port: int
    email: str
    db_uri: str
    smtp_host: str
    smtp_port: int
    smtp_login: str
    smtp_password: str
    smtp_email: str
    smtp_name: str


settings = Settings()
