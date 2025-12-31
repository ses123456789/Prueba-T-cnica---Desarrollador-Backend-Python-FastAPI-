from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    database_url: str = Field(..., alias="DATABASE_URL")

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
