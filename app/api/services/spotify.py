import requests
from app import config

SPOTIFY_CLIENT_ID = config.SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = config.SPOTIFY_CLIENT_SECRET
SPOTIFY_API_URL = config.SPOTIFY_API_URL
SPOTIFY_AUTH_URL = config.SPOTIFY_AUTH_URL


def get_spotify_access_token() -> str:
    url = f"{SPOTIFY_AUTH_URL}/token"
    auth = (SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    data = {"grant_type": 'client_credentials'}
    response = requests.post(url, auth=auth, data=data)
    response.raise_for_status()
    return response.json()['access_token']


def search_song(track_name: str):
    access_token = get_spotify_access_token()
    search_url = f"{SPOTIFY_API_URL}/v1/search?q={track_name}&type=track&limit=10"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        tracks = data['tracks']['items']
        track_info = []
        for idx, track in enumerate(tracks):
            album = track['album']
            largest_image = next((img['url'] for img in album['images'] if img['height'] == 300), None)
            track_info.append({
                "objectID": str(idx + 1),
                "track_name": track["name"],
                "artist_name": track["artist"],
                "album_name": album["name"],
                "image_url": largest_image,
                "url": track["external_urls"]["spotify"]
            })
        return track_info
    else:
        return {"error": "Failed to fetch data from Spotify"}
