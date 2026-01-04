"""Playlist-related routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/playlists", tags=["playlists"])


@router.post("/generate")
async def generate_playlist():
    """Generate a playlist based on run parameters."""
    # TODO: Implement in Sprint 4
    return {"message": "Generate playlist endpoint - to be implemented"}


@router.post("/save")
async def save_playlist():
    """Save generated playlist to Spotify."""
    # TODO: Implement in Sprint 5
    return {"message": "Save playlist endpoint - to be implemented"}

