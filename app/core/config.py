"""
Настройки приложения.

Загружает переменные из .env и валидирует их.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройки приложения."""
    
    # База данных
    database_url: str
    
    # API
    api_key: str = "change-me"
    
    # Режим отладки
    debug: bool = False
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()