"""Application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # API Settings
    API_V1_PREFIX: str = "/api"
    
    # CORS Settings
    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    # Spotify OAuth Settings
    SPOTIFY_CLIENT_ID: str = ""
    SPOTIFY_CLIENT_SECRET: str = ""
    SPOTIFY_REDIRECT_URI: str = "http://localhost:8000/api/auth/callback"
    
    # Session Settings
    SECRET_KEY: str = "change-me-in-production"  # Should be set via env var
    SESSION_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = True


settings = Settings()

