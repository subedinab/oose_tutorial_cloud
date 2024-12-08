# test_library.py

import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book(1, "Test Book", "Test Author")
        library.add_book(book)
        self.assertEqual(len(library.books), 1)

    def test_search_book(self):
        library = Library()
        book = Book(1, "Test Book", "Test Author")
        library.add_book(book)
        self.assertEqual(library.search_book("Test Book").title, "Test Book")

    def test_borrow_book(self):
        book = Book(1, "Test Book", "Test Author")
        self.assertTrue(book.borrow())
        self.assertFalse(book.borrow())

    def test_return_book(self):
        book = Book(1, "Test Book", "Test Author")
        book.borrow()
        self.assertTrue(book.return_book())
        self.assertFalse(book.return_book())

if __name__ == "__main__":
    unittest.main()
