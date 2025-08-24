from functools import lru_cache
from pydantic import AnyHttpUrl, PostgresDsn, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Union
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_file='.env', extra='ignore')

    # Backend
    SECRET_KEY: str = "a_very_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:5173"]

    # Database
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: Union[PostgresDsn, str] | None = None

    @model_validator(mode='after')
    def get_db_connection(self) -> 'Settings':
        if self.DATABASE_URI is None:
             self.DATABASE_URI = PostgresDsn.build(
                scheme="postgresql+psycopg2",
                username=self.POSTGRES_USER,
                password=self.POSTGRES_PASSWORD,
                host=self.POSTGRES_SERVER,
                path=f"/{self.POSTGRES_DB}",
            )
        return self

@lru_cache()
def get_settings() -> Settings:
    return Settings()
