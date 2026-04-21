from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Orbital Notify"
    debug: bool = False
    database_url: str = "sqlite:///database.db"

    class Config:
        env_file = ".env"   # Load from .env file if present
        env_file_encoding = "utf-8"
        case_sensitive = True

def get_settings() -> Settings:
    return Settings()