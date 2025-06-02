from pydantic import BaseModel
from typing import List

class Song(BaseModel):
    title: str
    artists: List[str]
    genre: str
    bpm: int
    file_path: str

