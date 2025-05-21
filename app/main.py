from fastapi import FastAPI
from app.routes import auth, books, readers, borrowed_books

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(readers.router, prefix="/readers", tags=["readers"])
app.include_router(borrowed_books.router, prefix="/borrow", tags=["borrow"])

@app.get("/")
def read_root():
    return {"message": "Library API is running! GO TO /docs"}
