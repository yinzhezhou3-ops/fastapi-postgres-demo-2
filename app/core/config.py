from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"

    class Config:
        env_file = ".env"
        extra = "ignore"  # 允许忽略 .env 里的额外变量

settings = Settings()