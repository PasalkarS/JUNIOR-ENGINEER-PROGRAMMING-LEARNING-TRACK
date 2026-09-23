# Business Workflow Layer
from models import Book
from repository import BookRepository

class LibraryService:
    def __init__(self, repo: BookRepository):
        self.repo = repo

    def add_new_book(self, book_id: str, title: str, author: str) -> Book:
        if not title.strip():
            raise ValueError("Book title cannot be blank.")
        book = Book(book_id, title.strip(), author.strip())
        self.repo.save(book)
        return book

    def list_books(self) -> list[Book]:
        return self.repo.find_all()
