# Application Entry Point
from repository import BookRepository
from service import LibraryService

def main():
    repo = BookRepository()
    service = LibraryService(repo)

    service.add_new_book("B1", "Clean Code", "Robert C. Martin")
    service.add_new_book("B2", "The Pragmatic Programmer", "David Thomas")

    print("Current Library Catalog:")
    for b in service.list_books():
        print(f" - [{b.book_id}] {b.title} by {b.author}")

if __name__ == "__main__":
    main()
