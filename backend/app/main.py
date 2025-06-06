from fastapi  import FastAPI, Depends, HTTPException, UploadFile, File 
from fastapi.staticfiles import StaticFiles
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

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/songs/")
def get_songs(session: SessionDep):
    return session.exec(select(Song)).all()

@app.get("/songs/{song_id}")
def get_song(song_id: int, session: SessionDep) -> Song:
    song = session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@app.delete("/remove-song/{song_id}")
async def delete_song(song_id: int, session: SessionDep) -> dict:
    song = session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    session.delete(song)
    session.commit()

    return{"message": f"Song '{song.title}' deleted successfully"}


@app.post("/add-song/")
async def create_song(song: Song, session: SessionDep ) -> Song:
        session.add(song)
        session.commit()
        session.refresh(song)
        return song

@app.post("/upload-file/")
async def upload_file(uploaded_file: UploadFile = File()):
    file_location = f"uploads/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())   
    
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}







app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)