from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field
from typing import Optional

class Settings(BaseSettings):
    # Database Configuration
    DATABASE_TYPE: str = "mysql"
    
    # MySQL Specific
    MYSQL_HOST: str = "localhost"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "password"
    MYSQL_DATABASE: str = "skincare_fix"
    MYSQL_PORT: int = 3306

    # Debug Setting
    DEBUG: bool = False

    # Computed Database URL
    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mysql+pymysql://{self.MYSQL_USER}:"
            f"{self.MYSQL_PASSWORD}@"
            f"{self.MYSQL_HOST}:"
            f"{self.MYSQL_PORT}/"
            f"{self.MYSQL_DATABASE}"
        )

    # Authentication Settings
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Pydantic Settings Configuration
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra='ignore'  # Ignore extra fields
    )

# Inisialisasi settings
settings = Settings()