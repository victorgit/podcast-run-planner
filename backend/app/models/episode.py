"""Episode data models."""

from pydantic import BaseModel


class Episode(BaseModel):
    """Episode model."""
    id: str
    name: str
    duration_ms: int
    description: str | None = None
    podcast_name: str
    podcast_id: str
    release_date: str | None = None

