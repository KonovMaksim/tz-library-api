from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas, database

router = APIRouter(prefix="/readers", tags=["readers"])

@router.post("/", response_model=schemas.ReaderResponse)
def create_reader(reader: schemas.ReaderCreate, db: Session = Depends(database.get_db)):
    return crud.reader.create_reader(db=db, reader=reader)

@router.get("/", response_model=List[schemas.ReaderResponse])
def read_readers(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.reader.get_readers(db=db, skip=skip, limit=limit)
