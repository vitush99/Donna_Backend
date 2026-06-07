from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "local"
    app_name: str = "Donna API"
    api_v1_prefix: str = "/v1"

    database_url: str = "sqlite:///./donna_dev.db"
    redis_url: str = "redis://localhost:6379/0"

    frontend_url: str = "http://localhost:3000"
    backend_cors_origins: str = "http://localhost:3000"

    jwt_secret_key: str = "replace-me"
    access_token_expire_minutes: int = 60

    openai_api_key: str | None = None
    anthropic_api_key: str | None = None

    google_client_id: str | None = None
    google_client_secret: str | None = None
    google_redirect_uri: str | None = None

    sentry_dsn: str | None = None
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.backend_cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
