
from models import Book


class LibraryService:
    def __init__(self, repository):
        self.repository = repository

    def add_new_book(self, book_id, title, author):
        if not book_id.strip():
            raise ValueError("Book ID is required")

        if not title.strip():
            raise ValueError("Book title is required")

        if not author.strip():
            raise ValueError("Author name is required")

        book = Book(
            book_id.strip(),
            title.strip(),
            author.strip()
        )

        self.repository.save(book)
        return book

    def list_books(self):
        return self.repository.find_all()

    def find_book(self, book_id):
        return self.repository.find_by_id(book_id)
