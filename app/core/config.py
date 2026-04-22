from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path(".env")
load_dotenv(dotenv_path)


def load_environment():
    """
    Loads environment variables from `.env` if it exists,
    otherwise from `.env.example`.
    """
    env_path = Path(".env")
    example_path = Path(".env.example")

    if env_path.is_file():
        print("Loading environment from .env")
        load_dotenv(dotenv_path=env_path)
    elif example_path.is_file():
        print("`.env` not found. Loading from .env.example")
        load_dotenv(dotenv_path=example_path)
    else:
        raise FileNotFoundError("Neither .env nor .env.example found.")

    # Optional: Validate required variables
    required_vars = ["DATABASE_URL", "APP_NAME"]
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"Missing required environment variables: {missing}")


try:
    load_environment()
    print("Environment variables loaded")
except Exception as e:
    print("Error: ", e)


class Settings(BaseSettings):
    app_name: str = os.getenv("APP_NAME")
    debug: bool = os.getenv("DEBUG")
    database_url: str = os.getenv("DATABASE_URL")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


def get_settings() -> Settings:
    return Settings()
