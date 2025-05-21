from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class BorrowedBookCreate(BaseModel):
    book_id: int
    reader_id: int

class BorrowedBookResponse(BaseModel):
    id: int
    book_id: int
    reader_id: int
    borrow_date: datetime
    return_date: Optional[datetime]

    class Config:
        from_attributes = True
