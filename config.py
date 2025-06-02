from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   DATABASE_URL: str
    APP_NAME: str = "Full Stack To Do App"

    class Config:
        env_file = ".env"
        extra = "ignore"


