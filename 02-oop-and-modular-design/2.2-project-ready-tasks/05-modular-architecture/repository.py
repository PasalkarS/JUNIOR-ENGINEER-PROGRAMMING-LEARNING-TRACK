
from models import Book


class BookRepository:
    def __init__(self):
        self.books = {}

    def save(self, book):
        self.books[book.book_id] = book

    def find_by_id(self, book_id):
        return self.books.get(book_id)

    def find_all(self):
        return list(self.books.values())
