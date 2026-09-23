# Persistence Layer
from models import Book

class BookRepository:
    def __init__(self):
        self._books: dict[str, Book] = {}

    def save(self, book: Book) -> None:
        self._books[book.book_id] = book

    def find_by_id(self, book_id: str) -> Book | None:
        return self._books.get(book_id)

    def find_all(self) -> list[Book]:
        return list(self._books.values())
