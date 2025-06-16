from fastapi  import FastAPI, Depends, HTTPException, UploadFile, File, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session, select
from typing import Annotated
from db.database import engine, get_session
from db.models import Song, User, CreateUser
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from passlib.context import CryptContext



@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


SessionDep = Annotated[Session, Depends(get_session)]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(session: SessionDep, username: str):
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()
    return user
    
def fake_decode_token(token: str, session: SessionDep):
    print(f"Decoding token: {token}")
    user = get_user(session, token)
    return user

def authenticate_user(session: SessionDep, username: str, password: str):
    user = get_user(session, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password)
        return False
    return user 


async def get_current_user(session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: SessionDep):
    user = get_user(session, form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    hashed_password = get_password_hash(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {"access_token": user.username, "token_type": "bearer"}



@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "artist_name": current_user.artist_name,
        "created_at": current_user.created_at
    }

@app.post("/register/")
async def register_user(user_data: CreateUser, session: SessionDep):
    existing_user = session.exec(
        select(User).where(User.username == user_data.username)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = get_password_hash(user_data.password)
    user = User(
        username=user_data.username,
        artist_name=user_data.artist_name,
        hashed_password=hashed_password
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user



    


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