from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # -----------------------------
    # Application Settings
    # -----------------------------
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str

    DEBUG: bool
    SQL_ECHO: bool

    HOST: str
    PORT: int

    # -----------------------------
    # Security
    # -----------------------------
    SECRET_KEY: str

    # -----------------------------
    # Database
    # -----------------------------
    DATABASE_URL: str

    # -----------------------------
    # Ollama
    # -----------------------------
    OLLAMA_BASE_URL: str
    OLLAMA_MODEL: str

    # -----------------------------
    # Embeddings
    # -----------------------------
    EMBEDDING_MODEL: str

    # -----------------------------
    # FAISS
    # -----------------------------
    FAISS_INDEX_PATH: str
    FAISS_METADATA_PATH: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

    @field_validator("DEBUG", "SQL_ECHO", mode="before")
    @classmethod
    def parse_bool_like_values(cls, value):
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in {"release", "production", "prod", "false", "0", "off", "no"}:
                return False
            if normalized in {"debug", "development", "dev", "true", "1", "on", "yes"}:
                return True
        return value


settings = Settings()
