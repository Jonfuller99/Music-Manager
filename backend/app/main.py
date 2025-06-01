from fastapi  import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Annotated, Session
from db import engine, get_session, Song, SQLModel
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
    return session.query(Song).all()

@app.get("/api/hello")
async def read_root():
    return {"message": "hello this is the fast api working"}