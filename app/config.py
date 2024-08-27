import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "CoverTwin"
VERSION = "0.1.0"
DESCRIPTION = "Find songs and albums with similar cover art"

API_V1_STR = "/api/v1"

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_API_URL = os.getenv("SPOTIFY_API_URL")
SPOTIFY_AUTH_URL = os.getenv("SPOTIFY_AUTH_URL")

LAST_FM_API_KEY = os.getenv("LAST_FM_API_KEY")

ALGOLIA_APP_ID = os.getenv("ALGOLIA_APP_ID")
ALGOLIA_API_KEY = os.getenv("ALGOLIA_API_KEY")
ALGOLIA_SONGS_INDEX_NAME = os.getenv("ALGOLIA_SONGS_INDEX_NAME", "songs")
ALGOLIA_ALBUMS_INDEX_NAME = os.getenv("ALGOLIA_ALBUMS_INDEX_NAME", "albums")

BACKEND_CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://tbd.com"
]


# I might implement caching
CACHE_TTL = 60 * 60

RATE_LIMIT = "100/minute"

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

ENABLE_ALBUM_SEARCH = os.getenv("ENABLE_ALBUM_SEARCH", "True").lower() == "true"
ENABLE_SONG_SEARCH = os.getenv("ENABLE_SONG_SEARCH", "True").lower() == "true"

SECRET_KEY = os.getenv("SECRET_KEY", "secret")


required_env_vars = [
    "SPOTIFY_CLIENT_ID",
    "SPOTIFY_CLIENT_SECRET",
    "ALGOLIA_APP_ID",
    "ALGOLIA_API_KEY",
]

for var in required_env_vars:
    if not locals().get(var):
        raise EnvironmentError(f"Missing environment variable: {var}")