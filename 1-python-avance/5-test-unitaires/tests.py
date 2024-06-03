# test_library.py

import unittest
from main import Book, Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
        self.book2 = Book("1984", "George Orwell")
        self.book3 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)

    def test_add_book(self):
        new_book = Book("Brave New World", "Aldous Huxley")
        self.library.add_book(new_book)
        self.assertIn(new_book, self.library.books)

    def test_find_books_by_title(self):
        results = self.library.find_books_by_title("1984")
        self.assertIn(self.book2, results)
        self.assertNotIn(self.book1, results)

    def test_find_books_by_author(self):
        results = self.library.find_books_by_author("Harper Lee")
        self.assertIn(self.book3, results)
        self.assertNotIn(self.book1, results)

    def test_check_out_book(self):
        self.library.check_out_book("1984")
        self.assertTrue(self.book2.is_checked_out)
        with self.assertRaises(ValueError):
            self.library.check_out_book("1984")

    def test_return_book(self):
        self.library.check_out_book("1984")
        self.library.return_book("1984")
        self.assertFalse(self.book2.is_checked_out)
        with self.assertRaises(ValueError):
            self.library.return_book("1984")

    def test_check_out_book_not_found(self):
        with self.assertRaises(ValueError):
            self.library.check_out_book("Not a Book")

    def test_return_book_not_found(self):
        with self.assertRaises(ValueError):
            self.library.return_book("Not a Book")

if __name__ == '__main__':
    unittest.main()
