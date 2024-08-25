from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import config

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
