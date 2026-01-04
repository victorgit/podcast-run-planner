"""Spotify API client."""

# TODO: Implement in Sprint 1-2
# This will handle all Spotify API interactions


class SpotifyClient:
    """Client for interacting with Spotify API."""
    
    def __init__(self, access_token: str):
        """Initialize Spotify client with access token."""
        self.access_token = access_token
    
    async def get_user_profile(self):
        """Get current user's profile."""
        # TODO: Implement in Sprint 1
        raise NotImplementedError("Not yet implemented")
    
    async def get_saved_episodes(self, limit: int = 50, offset: int = 0):
        """Get user's saved episodes."""
        # TODO: Implement in Sprint 2
        raise NotImplementedError("Not yet implemented")
    
    async def get_followed_podcasts(self):
        """Get user's followed podcasts."""
        # TODO: Implement in Sprint 2
        raise NotImplementedError("Not yet implemented")
    
    async def create_playlist(self, name: str, description: str = ""):
        """Create a new playlist."""
        # TODO: Implement in Sprint 5
        raise NotImplementedError("Not yet implemented")
    
    async def add_episodes_to_playlist(self, playlist_id: str, episode_uris: list[str]):
        """Add episodes to a playlist."""
        # TODO: Implement in Sprint 5
        raise NotImplementedError("Not yet implemented")

