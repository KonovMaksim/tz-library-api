from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas, database

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.book.create_book(db=db, book=book)

@router.get("/", response_model=List[schemas.BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.book.get_books(db=db, skip=skip, limit=limit)
