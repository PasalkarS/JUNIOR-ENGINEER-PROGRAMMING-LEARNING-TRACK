
from repository import BookRepository
from service import LibraryService


def main():
    repository = BookRepository()
    service = LibraryService(repository)

    service.add_new_book(
        "B1", "Clean Code", "Robert C. Martin"
    )

    service.add_new_book(
        "B2", "The Pragmatic Programmer", "David Thomas"
    )

    print("Library Catalog:")

    for book in service.list_books():
        print("Book ID:", book.book_id)
        print("Title:", book.title)
        print("Author:", book.author)
        print("-------------------")


if __name__ == "__main__":
    main()
