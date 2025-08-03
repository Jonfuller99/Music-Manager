from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List
from datetime import datetime, timezone
from enum import Enum

class Song(SQLModel, table=True):
    song_id: int | None = Field(default=None, primary_key = True)
    title: str = Field(index=True)
    artist: str = Field(index=True)
    genre: str = Field(index=True)
    bpm: int = Field(index=True)
    file_path: str = Field(index=True)
    uploaded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    song_artists: List["SongArtist"] = Relationship(back_populates="song")

class UserRole(str, Enum):
    ADMIN = 'admin'
    USER = 'user'

class Artist(SQLModel, table=True):
    artist_id: int = Field(default=None, primary_key= True)
    name: str = Field(index=True) 
    user_id: int | None  = Field(foreign_key="users.user_id")

    user: Optional["User"] = Relationship(back_populates="artist")
    songs: List["SongArtist"] = Relationship(back_populates="artist")


class User(SQLModel, table=True):
    __tablename__ = 'users'
    user_id: int = Field(default=None, primary_key= True)
    username: str = Field(index=True)
    hashed_password: str
    disabled: bool | None = None
    role: UserRole = Field(default=UserRole.USER)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    artist: Optional[Artist] = Relationship(back_populates="user")

class SongArtist(SQLModel, table=True):
    song_id: int = Field(foreign_key="song.song_id", primary_key=True)
    artist_id: int = Field(foreign_key="artist.artist_id", primary_key=True)

    song: Song = Relationship(back_populates="song_artists")
    artist: Artist = Relationship(back_populates="songs")

class CreateUser(SQLModel):
    username: str
    artist_id: int
    password: str  

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    username: str | None = None