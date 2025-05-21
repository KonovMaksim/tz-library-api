from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas, database

router = APIRouter(prefix="/borrow", tags=["borrow"])

@router.post("/", response_model=schemas.BorrowedBookResponse)
def borrow_book(borrow: schemas.BorrowedBookCreate, db: Session = Depends(database.get_db)):
    return crud.borrowed_book.borrow_book(db=db, borrow=borrow)

@router.post("/return/")
def return_book(borrow: schemas.BorrowedBookCreate, db: Session = Depends(database.get_db)):
    return crud.borrowed_book.return_book(db=db, borrow=borrow)
