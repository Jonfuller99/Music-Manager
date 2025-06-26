from fastapi  import FastAPI, Depends, HTTPException, UploadFile, File, status, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session, select
from typing import Annotated
from db.database import engine, get_session
from db.models import Artist, Song, User, CreateUser, TokenData, Token, UserRole
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from passlib.context import CryptContext
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import yt_dlp as youtube_dl 
import tempfile 
import jwt
import os



load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


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
    
def decode_token(token: str, session: SessionDep):
    print(f"Decoding token: {token}")
    user = get_user(session, token)
    return user

def authenticate_user(session: SessionDep, username: str, password: str):
    user = get_user(session, username)
    
    if not user:
        return {
            'user': False,
            "msg": f"No account found with username: '{username}'"
        }            
    if not verify_password(password, user.hashed_password):
        return {
            'user': False,
            'msg': 'Incorrect password'
        }
    return {
        'user': user,
        'msg': ''
    }

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,  algorithm = ALGORITHM)
    return encoded_jwt


async def get_current_user(session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(session, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def require_admin(current_user: Annotated[User, Depends(get_current_active_user)]):
    print(f"[DEBUG] User: {current_user.username}, Role: {current_user.role} ({type(current_user.role)})")
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=400, detail='Requires admin access')
    return current_user


@app.post("/token/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: SessionDep) -> Token:
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user['user']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=user['msg'],
            headers={"WWW-Authenticate": "Bearer"},
            )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['user'].username}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")



@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    if current_user.artist is None:
        artist_name = current_user.username
    else:
        artist_name = current_user.artist.name
    
    return {
        "id": current_user.user_id,
        "username": current_user.username,
        "artist_name": artist_name,
        "role": current_user.role,
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

    artist = session.get(Artist,  user_data.artist_id)
    user = User(
        username=user_data.username,
        hashed_password=hashed_password
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    if artist is not None:
        artist.user_id = user.user_id
        session.add(artist)
        session.commit()

    return user



    


@app.get("/songs/")
def get_songs(session: SessionDep):
    return session.exec(select(Song)).all()

@app.get("/artists/")
def get_artists(session: SessionDep):
    return session.exec(select(Artist)).all()

@app.get("/songs/{song_id}")
def get_song(song_id: int, session: SessionDep) -> Song:
    song = session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@app.delete("/remove-song/{song_id}") #requires admin
async def delete_song(song_id: int, session: SessionDep, admin_user: Annotated[User, Depends(require_admin)]) -> dict:
    song = session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    session.delete(song)
    session.commit()

    return{"message": f"Song '{song.title}' deleted successfully"}


@app.post("/add-song/") #requires admin
async def create_song(song: Song, session: SessionDep, admin_user: Annotated[User, Depends(require_admin)] ) -> Song:
        session.add(song)
        session.commit()
        session.refresh(song)
        return song

@app.post("/upload-file/")
async def upload_file(admin_user: Annotated[User, Depends(require_admin)], uploaded_file: UploadFile = File()):
    file_location = f"uploads/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())   
    
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}


@app.get("/link-to-mp3/")
async def link_to_mp3(url: str = Query(...)):
    print('at backend')
    try:
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'quiet': False,
            'no_warnings': False,
            'writeinfojson': False,
            'writethumbnail': False,
            'writesubtitles': False,
            'extractaudio': True,
            'audioformat': 'mp3',
            'audioquality': '192k', 
        }
        
        with youtube_dl.YoutubeDL(options) as ydl:

            info = ydl.extract_info(url, download=False)
            audio_url = info.get('url')

            return {
                'title': info.get('title'),
                'duration': info.get('duration'),
                'audio_url': audio_url,
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
        






app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)