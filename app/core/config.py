from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    app_name: str = "JEE-Sense AI"
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
settings = Settings()
