from sqlalchemy.orm import Session
from app.models.reader import Reader
from app.schemas.reader import ReaderCreate, ReaderResponse

def get_readers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Reader).offset(skip).limit(limit).all()

def create_reader(db: Session, reader: ReaderCreate) -> ReaderResponse:
    db_reader = Reader(**reader.dict())
    db.add(db_reader)
    db.commit()
    db.refresh(db_reader)
    return db_reader
