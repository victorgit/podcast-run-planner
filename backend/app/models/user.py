"""User data models."""

from pydantic import BaseModel


class User(BaseModel):
    """User model."""
    id: str
    display_name: str
    email: str | None = None

