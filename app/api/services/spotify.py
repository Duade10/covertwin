import requests
from PIL import image
from io import BytesIO
import json
from app import config

SPOTIFY_CLIENT_ID = config.SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = config.SPOTIFY_CLIENT_SECRET
SPOTIFY_API_URL = config.SPOTIFY_API_URL


def get_spotify_access_token():
    url = f"{SPOTIFY_API_URL}/token"
    auth = (SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    data = {"grant_type": 'client_credentials'}
    response = requests.post(url, auth=auth, data=data)
    response.raise_for_status()
    return response.json()['access_token']


def fetch_song(track_name: str):
    access_token = get_spotify_access_token()
    search_url = f"{}"