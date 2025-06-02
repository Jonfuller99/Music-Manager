from fastapi  import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from typing import Annotated
from db.database import engine, get_session
from db.models import Song
from sqlmodel import SQLModel
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)


SessionDep = Annotated[Session, Depends(get_session)]


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



@app.get("/songs/")
def get_songs(session: SessionDep):
    return session.exec(select(Song)).all()

@app.get("/songs/{song_id}")
def get_song(song_id: int, session: SessionDep) -> Song:
    song = session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@app.post("/add-song/")
def create_song(song: Song, session: SessionDep) -> Song:
    session.add(song)
    session.commit()
    session.refresh(song)
    return song

@app.get("/api/hello")
async def read_root():
    return {"message": "hello this is the fast api working"}