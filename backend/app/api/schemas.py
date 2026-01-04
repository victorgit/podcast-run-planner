"""Pydantic schemas for request/response models."""

from pydantic import BaseModel


# Episode Models
class Episode(BaseModel):
    """Episode model."""
    id: str
    name: str
    duration_ms: int
    description: str | None = None
    podcast_name: str
    podcast_id: str
    release_date: str | None = None


# Playlist Models
class PlaylistGenerationRequest(BaseModel):
    """Request model for playlist generation."""
    duration_minutes: int
    run_type: str  # "easy" | "tempo" | "long"
    content_preference: str  # "light" | "mixed" | "deep"


class PlaylistItem(BaseModel):
    """Item in a generated playlist."""
    episode: Episode
    order: int


class Playlist(BaseModel):
    """Generated playlist model."""
    items: list[PlaylistItem]
    total_duration_minutes: float
    target_duration_minutes: int


class SavePlaylistRequest(BaseModel):
    """Request model for saving playlist."""
    playlist_name: str
    episode_ids: list[str]

