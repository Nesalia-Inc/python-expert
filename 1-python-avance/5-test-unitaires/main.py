from dataclasses import dataclass


@dataclass
class Book:
    title : str
    author : str
    
    def __post_init__(self) -> None:
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            raise ValueError("Book is already checked out")
        self.is_checked_out = True

    def return_book(self):
        if not self.is_checked_out:
            raise ValueError("Book is not checked out")
        self.is_checked_out = False


class Library:
    def __init__(self) -> None:
        self.books : list[Book] = []

    def add_book(self, book : Book):
        self.books.append(book)

    def find_books_by_title(self, title : str) -> list[Book]:
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_books_by_author(self, author : str) -> list[Book]:
        return [book for book in self.books if author.lower() in book.author.lower()]

    def check_out_book(self, title : str) -> Book:
        for book in self.books:
            if book.title == title:
                book.check_out()
                return book
        raise ValueError("Book not found")

    def return_book(self, title : str) -> Book:
        for book in self.books:
            if book.title == title:
                book.return_book()
                return book
        raise ValueError("Book not found")
