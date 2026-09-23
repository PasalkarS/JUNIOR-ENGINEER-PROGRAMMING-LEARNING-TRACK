# Domain Models
class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __repr__(self) -> str:
        return f"Book({self.book_id!r}, {self.title!r}, {self.author!r})"
