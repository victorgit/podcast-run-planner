"""Playlist data models."""

from pydantic import BaseModel


class Playlist(BaseModel):
    """Playlist model."""
    id: str
    name: str
    description: str | None = None
    spotify_url: str | None = None

