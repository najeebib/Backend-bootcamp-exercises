from .book import Book
from collections import Counter

class ImprovedLibrary:
    def __init__(self):
        self.books = {}
    # time complexity: O(1)
    def add_book(self, bookname):
        if bookname not in self.books:
            self.books[bookname] = Book(bookname)
    # time complexity: O(1)
    def borrow_book(self, book):
        if book in self.books:
            self.books[book].increment_burrow()

    # time complexity: O(n)
    def most_borrowed_book(self):
        if not self.books:
            return None
        max_borrow_count = -1
        most_borrowed_book = None
        for book in self.books:
            if book.borrow_count > max_borrow_count:
                max_borrow_count = book.borrow_count
                most_borrowed_book = book
        return most_borrowed_book


