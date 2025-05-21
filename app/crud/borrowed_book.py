from datetime import datetime
from sqlalchemy.orm import Session
from app.models.borrowed_book import BorrowedBook
from app.models.book import Book
from app.schemas.borrowed_book import BorrowedBookCreate, BorrowedBookResponse


def borrow_book(db: Session, borrow: BorrowedBookCreate) -> BorrowedBookResponse:
    book = db.query(Book).filter(Book.id == borrow.book_id).first()
    if not book or book.copies_available <= 0:
        raise ValueError("Book not available")

    borrowed_count = db.query(BorrowedBook).filter(
        BorrowedBook.reader_id == borrow.reader_id,
        BorrowedBook.return_date.is_(None)
    ).count()

    if borrowed_count >= 3:
        raise ValueError("Reader has reached the borrowing limit")

    book.copies_available -= 1
    new_borrow = BorrowedBook(
        book_id=borrow.book_id,
        reader_id=borrow.reader_id,
        borrow_date=datetime.utcnow()
    )
    db.add(new_borrow)
    db.commit()
    db.refresh(new_borrow)
    return new_borrow


def return_book(db: Session, borrow: BorrowedBookCreate):
    borrowed = db.query(BorrowedBook).filter(
        BorrowedBook.book_id == borrow.book_id,
        BorrowedBook.reader_id == borrow.reader_id,
        BorrowedBook.return_date.is_(None)
    ).first()

    if not borrowed:
        raise ValueError("Book not borrowed by this reader")

    borrowed.return_date = datetime.utcnow()
    book = db.query(Book).filter(Book.id == borrow.book_id).first()
    if book:
        book.copies_available += 1
    db.commit()
    return {"message": "Book returned successfully"}