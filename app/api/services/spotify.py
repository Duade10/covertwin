import requests
from app import config
import re

SPOTIFY_CLIENT_ID = config.SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = config.SPOTIFY_CLIENT_SECRET
SPOTIFY_API_URL = config.SPOTIFY_API_URL
SPOTIFY_AUTH_URL = config.SPOTIFY_AUTH_URL


def extract_artist_id(spotify_uri: str):
    # Regular expression to extract the artist ID from the URI
    match = re.search(r'spotify:artist:([a-zA-Z0-9]+)', spotify_uri)

    if match:
        return match.group(1)  # Return the extracted artist ID
    else:
        return None  # Return None if the ID is not found


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
                "track_id": track["id"],
                "track_name": track["name"],
                "artist_name": track["artists"][0]["name"],
                "artist_uri": extract_artist_id(track["artists"][0]["uri"]),
                "album_name": album["name"],
                "image_url": largest_image,
                "url": track["external_urls"]["spotify"]
            })
        return track_info
    else:
        return {"error": "Failed to fetch data from Spotify"}


def get_artist_info(artist_id: str):
    access_token = get_spotify_access_token()
    artist_url = f"{SPOTIFY_API_URL}/v1/artists/{artist_id}"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(artist_url, headers=headers)

    if response.status_code == 200:
        artist_data = response.json()
        print(artist_data)
        return {
            "artist_id": artist_data["id"],
            "genres": artist_data["genres"]  # List of genres
        }
    else:
        print(response.status_code)
        return {
            "artist_id": artist_id,
            "genres": []
        }
