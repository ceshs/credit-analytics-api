from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Credit Analytics API"
    app_env: str = "development"
    debug: bool = Field(default=True, validation_alias="APP_DEBUG")
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/credit_analytics"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
