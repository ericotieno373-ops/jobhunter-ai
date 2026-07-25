from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    OPENAI_API_KEY: str = ""
    TELEGRAM_TOKEN: str = ""
    TELEGRAM_CHAT_ID: str = ""
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )
    CORPORATE_STAFFING_URL: str

settings = Settings()