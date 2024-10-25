# database.py
from peewee import SqliteDatabase, Model, CharField, FloatField, IntegerField
from typing import List, Dict, Optional
import csv
import os

# Initialize SQLite database
db = SqliteDatabase('bookstore.db')
csv_path = 'bookstore.csv'

# Define the Book model with Peewee ORM
class Book(Model):
    name = CharField()
    author = CharField()
    isbn = CharField(unique=True)
    price = FloatField()
    copies = IntegerField()

    class Meta:
        database = db

# Define the Bookstore class
class Bookstore:
    def __init__(self, db_path: str = 'bookstore.db', csv_path: str = csv_path):
        """Initialize the Bookstore with an SQLite database."""
        self.db = SqliteDatabase(db_path)
        Book._meta.database = self.db  # Bind the database to the Book model
        self.db.connect()
        self.db.create_tables([Book], safe=True)

        # Populate the database if empty
        if not Book.select().exists():
            self._populate_from_csv(csv_path)

    def _populate_from_csv(self, csv_path: str):
        """Populate the database with data from a CSV file."""
        if not os.path.exists(csv_path):
            print(f"CSV file '{csv_path}' not found.")
            return

        with open(csv_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_book(
                    name=row['name'],
                    author=row['author'],
                    isbn=row['isbn'],
                    price=float(row['price']),
                    copies=int(row['copies'])
                )
        print(f"Database populated with data from '{csv_path}'.")

    def reset_test_data(self) -> None:
        """Reset test data for book store."""
        with self.db.atomic():
            try:
                Book.delete().execute()
                self._populate_from_csv(csv_path = csv_path)
            except Exception as e:
                raise e

    def list_books(self) -> List[Dict]:
        """Return a list of all books in the store."""
        with self.db.atomic():
            books = Book.select()
            return [{"name": book.name, "author": book.author, "isbn": book.isbn, "price": book.price, "copies": book.copies} for book in books]

    def add_book(self, name: str, author: str, isbn: str, price: float, copies: int) -> int:
        """Add a new book to the store and return its ID."""
        with self.db.atomic():
            new_book = Book.create(name=name, author=author, isbn=isbn, price=price, copies=copies)
            return new_book.id

    def remove_book(self, isbn: str) -> None:
        """Remove a book from the store by ISBN."""
        with self.db.atomic():
            try:
                book = Book.get(Book.isbn == isbn)
                book.delete_instance()
            except Book.DoesNotExist:
                raise ValueError("Book not found")

    def sell_book(self, isbn: str) -> None:
        """Sell a book by decreasing its copy count by one."""
        with self.db.atomic():
            try:
                book = Book.get(Book.isbn == isbn)
                if book.copies > 0:
                    book.copies -= 1
                    book.save()
                else:
                    raise ValueError("No copies available")
            except Book.DoesNotExist:
                raise ValueError("Book not found")

    def get_book_by_isbn(self, isbn: str) -> Dict:
        """Get a book's data by ISBN."""
        with self.db.atomic():
            try:
                book = Book.get(Book.isbn == isbn)
                return {"name": book.name, "author": book.author, "isbn": book.isbn, "price": book.price, "copies": book.copies}
            except Book.DoesNotExist:
                raise ValueError("Book not found")

    def search_books(self, name: Optional[str] = None, author: Optional[str] = None, isbn: Optional[str] = None) -> List[Dict]:
        """Search books with optional filters for name, author, and ISBN. Supports partial matches and returns all if filters are empty."""
        with self.db.atomic():
            query = Book.select()
            if name:
                query = query.where(Book.name.contains(name))
            if author:
                query = query.where(Book.author.contains(author))
            if isbn:
                query = query.where(Book.isbn.contains(isbn))

            # Return results directly; no error is raised if nothing is found
            return [{"name": book.name, "author": book.author, "isbn": book.isbn, "price": book.price, "copies": book.copies} for book in query]

    def update_book(self, isbn: str, name: Optional[str] = None, author: Optional[str] = None, new_isbn: Optional[str] = None, price: Optional[float] = None, copies: Optional[int] = None) -> None:
        """Update a book's details using the given ISBN."""
        with self.db.atomic():
            try:
                book = Book.get(Book.isbn == isbn)
                if name is not None:
                    book.name = name
                if author is not None:
                    book.author = author
                if new_isbn is not None:
                    book.isbn = new_isbn
                if price is not None:
                    book.price = price
                if copies is not None:
                    book.copies = copies
                book.save()
            except Book.DoesNotExist:
                raise ValueError("Book not found")
