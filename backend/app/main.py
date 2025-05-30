from fastapi  import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models.models import Song

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {
        "message": "this is the main page",
        "age": 12,
        "songs" : [
            {"title" : "Never Cared", "artists": ['Cdug', 'Mr.J'], "beat": "snakesandrakes.mp3"},
        ],
        "url": "http://localhost:8000/api/hello" 
    }

@app.get("/songs", response_model=List[Song])
async def get_songs():
    return [
        Song(title="Never Cared", artists=["Mr.J", "Cdug" ], genre="Hip Hop", beat="SnakesAndRakes.mp3"), #TODO add genres as as table in DB
        Song(title="Fantastic4", artists=["Mr.J", "Big Tasty", "JPXFRD", "Cdug" ], genre="Hip Hop", beat="Magic.mp3") 
    ]

@app.get("/api/hello")
async def read_root():
    return {"message": "hello this is the fast api working"}