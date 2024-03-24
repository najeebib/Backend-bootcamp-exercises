class Book:
    def __init__(self, name):
        self.name = name
        self.borrow_count = 0
    # time complexity: O(1)
    def increment_burrow(self):
        self.borrow_count += 1