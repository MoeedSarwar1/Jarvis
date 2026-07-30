from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str | None = None
    openrouter_api_key: str
    openrouter_base_url: str
    openai_base_url: str | None = None
    ai_model: str | None = None

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore[call-arg]
