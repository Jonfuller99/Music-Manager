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