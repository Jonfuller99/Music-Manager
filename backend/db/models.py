from sqlmodel import Field, SQLModel
from datetime import datetime, timezone

class Song(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key = True)
    title: str = Field(index=True)
    artist: str = Field(index=True)
    genre: str = Field(index=True)
    bpm: int = Field(index=True)
    file_path: str = Field(index=True)
    uploaded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key= True)
    username: str = Field(index=True)
    artist_name: str = Field(index=True) 
    hashed_password: str
    disabled: bool | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class CreateUser(SQLModel):
    username: str
    artist_name: str
    password: str  

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    username: str | None = None