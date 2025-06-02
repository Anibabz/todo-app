from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    app_name: str = "Full Stack To Do App"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

