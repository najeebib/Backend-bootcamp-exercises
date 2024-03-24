class Library:
    def __init__(self):
        self.books = []
    # time complexity: O(n)
    def add_book(self, book):
        self.books.append(book)
    # time complexity: O(1)
    def borrow_book(self, book):
        book.increment_burrow()
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
