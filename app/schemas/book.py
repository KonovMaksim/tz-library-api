from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    isbn: Optional[str] = None
    copies_available: int = 1
    description: Optional[str] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int]
    isbn: Optional[str]
    copies_available: int
    description: Optional[str]

    class Config:
        from_attributes = True
