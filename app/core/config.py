import os
from pydantic import BaseSettings, AnyHttpUrl, SecretStr

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    JWT_SECRET: SecretStr = SecretStr(os.getenv("JWT_SECRET", "supersecret"))
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    CORS_ORIGINS: list[AnyHttpUrl] = ["http://localhost:3000"]
    OAUTH_GOOGLE_CLIENT_ID: str = os.getenv("OAUTH_GOOGLE_CLIENT_ID")
    OAUTH_GOOGLE_CLIENT_SECRET: SecretStr = SecretStr(os.getenv("OAUTH_GOOGLE_CLIENT_SECRET"))
    OAUTH_GITHUB_CLIENT_ID: str = os.getenv("OAUTH_GITHUB_CLIENT_ID")
    OAUTH_GITHUB_CLIENT_SECRET: SecretStr = SecretStr(os.getenv("OAUTH_GITHUB_CLIENT_SECRET"))

settings = Settings()