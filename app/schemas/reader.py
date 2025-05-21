from pydantic import BaseModel

class ReaderCreate(BaseModel):
    name: str
    email: str

class ReaderResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True