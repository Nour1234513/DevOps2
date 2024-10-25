# main.py
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
from database import Bookstore
import uvicorn

# Initialize FastAPI app and Bookstore instance
app = FastAPI(title='BookStore', docs_url='/', description="BookStore API", version='1.0.0')
bookstore = Bookstore()  # Create a Bookstore instance

# Define Book request model for adding a new book
class BookRequestResponseModel(BaseModel):
    name: str
    author: str
    isbn: str
    price: float
    copies: int

# Define Book request model for updating a book
class BookUpdateRequestModel(BaseModel):
    name: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    price: Optional[float] = None
    copies: Optional[int] = None

class MessageResponseModel(BaseModel):
    message: str

class ErrorResponseModel(BaseModel):
    detail: str

# Define the FastAPI endpoints

@app.get("/books", operation_id='list_books', response_model=list[BookRequestResponseModel], tags=["actions"], responses={400: {"model": ErrorResponseModel}})
def list_books():
    """List all books in the store."""
    return bookstore.list_books()

@app.post("/books", operation_id='add_book', tags=["actions"])
def add_book(book: BookRequestResponseModel):
    """Add a new book to the store."""
    try:
        book_id = bookstore.add_book(
            name=book.name,
            author=book.author,
            isbn=book.isbn,
            price=book.price,
            copies=book.copies
        )
        return {"message": "Book added successfully", "book_id": book_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/books/{isbn}", operation_id='delete_book', response_model=MessageResponseModel, tags=["actions"], responses={400: {"model": ErrorResponseModel}, 404: {"model": ErrorResponseModel}})
def remove_book(isbn: str):
    """Remove a book from the store by ISBN."""
    try:
        bookstore.remove_book(isbn)
        return MessageResponseModel(message="Book removed successfully")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/books/sell/{isbn}", operation_id='sell_book', response_model=MessageResponseModel, tags=["actions"], responses={400: {"model": ErrorResponseModel}, 404: {"model": ErrorResponseModel}, 409: {"model": ErrorResponseModel}})
def sell_book(isbn: str):
    """Sell a book by decreasing its copy count by one."""
    try:
        bookstore.sell_book(isbn)
        return MessageResponseModel(message="Book sold successfully")
    except ValueError as e:
        if e == "Book not found":
            raise HTTPException(status_code=404, detail=str(e))
        if e == "No copies available":
            raise HTTPException(status_code=409, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/books/search", operation_id='search_book', response_model=list[BookRequestResponseModel], tags=["actions"], responses={400: {"model": ErrorResponseModel}})
def search_books(name: Optional[str] = None, author: Optional[str] = None, isbn: Optional[str] = None):
    """Search for books using optional filters for name, author, and ISBN."""
    try:
        books = bookstore.search_books(name=name, author=author, isbn=isbn)
        return books
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/books/{isbn}", operation_id='get_book', response_model=BookRequestResponseModel, tags=["actions"], responses={400: {"model": ErrorResponseModel}, 404: {"model": ErrorResponseModel}})
def get_book_by_isbn(isbn: str):
    """Retrieve a book's data by ISBN."""
    try:
        book = bookstore.get_book_by_isbn(isbn)
        return book
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.patch("/books/{isbn}", operation_id='update_book', response_model=MessageResponseModel, tags=["actions"], responses={400: {"model": ErrorResponseModel}, 404: {"model": ErrorResponseModel}})
def update_book(isbn: str, book: BookUpdateRequestModel):
    """Update a book's information based on ISBN."""
    try:
        bookstore.update_book(
            isbn=isbn,
            name=book.name,
            author=book.author,
            new_isbn=book.isbn,
            price=book.price,
            copies=book.copies
        )
        return MessageResponseModel(message="Book updated successfully")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/reset", operation_id='reset_test_data', response_model=MessageResponseModel, tags=["actions"], responses={500: {"model": ErrorResponseModel}})
def reset_test_data():
    """Reset test data for book store."""
    try:
        bookstore.reset_test_data()
        return MessageResponseModel(message="Test data successfully reset")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Add the entry point for running the server directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
