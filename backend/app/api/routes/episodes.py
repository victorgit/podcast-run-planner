"""Episode-related routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/episodes", tags=["episodes"])


@router.get("")
async def get_episodes(limit: int = 50, offset: int = 0):
    """Get user's saved episodes and followed podcasts."""
    # TODO: Implement in Sprint 2
    return {"message": "Episodes endpoint - to be implemented", "limit": limit, "offset": offset}


@router.get("/{episode_id}")
async def get_episode(episode_id: str):
    """Get episode details."""
    # TODO: Implement in Sprint 2
    return {"message": "Episode detail endpoint - to be implemented", "episode_id": episode_id}

