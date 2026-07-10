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


settings = Settings()