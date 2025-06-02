from sqlalchemy import create_engine
from sqlmodel import Session


DATABASE_URL = "postgresql://postgres:password@db:5432/musicdb"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session