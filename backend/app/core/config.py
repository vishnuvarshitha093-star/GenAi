from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Workplace Access System"
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/workplace"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    token_expire_minutes: int = 60


settings = Settings()
