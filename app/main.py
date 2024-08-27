from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import config
from app.api.services import spotify

app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to CoverTwin API!"}


@app.get("/search/{track_name}")
async def find_song(track_name: str):
    songs = spotify.search_song(track_name)
    return {"songs": songs}
