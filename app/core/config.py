from pydantic_settings import BaseSettings, SettingsConfigDict


def get_settings() -> Settings:
    return Settings()


class Settings(BaseSettings):
    app_name: str = "Orbital Notify"
    debug: bool = False
    database_url: str = "sqlite:///database.db"

    settings_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        validate_default=False,
    )