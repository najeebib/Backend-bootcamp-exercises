from modules.book import Book
from modules.library import Library
from modules.improved_library import ImprovedLibrary
import time
def measure(library):
        book1 = Book("book1")
        book2 = Book("book2")
        
        
        start_time = time.perf_counter()
        for _ in range(3):
            library.add_book(book1)
            library.add_book(book2)
        end_time = time.perf_counter()
        total = end_time - start_time
        add_book_time = (total) / 3
        
        start_time = time.perf_counter()
        for _ in range(3):
            library.borrow_book(book1)
            library.borrow_book(book2)
        end_time = time.perf_counter()
        total = end_time - start_time
        borrow_book_time = (total) / 3
        
        start_time = time.perf_counter()
        for _ in range(3):
            most_borrowed_book = library.most_borrowed_book()
        end_time = time.perf_counter()
        total = end_time - start_time
        most_borrowed_book_time = (total) / 3
        
        with open('performance_results.txt', 'a') as f:
            f.write(f"add book\t{add_book_time}\n")
            f.write(f"borrow book\t{borrow_book_time}\n")
            f.write(f"get most borrowed book\t{most_borrowed_book_time}\n")
            f.write("\n\n")


def main():
    f = open('performance_results.txt', 'w')
    f.close()
    library = Library()
    measure(library=library)
    improved_library = ImprovedLibrary()
    measure(library=improved_library)

if __name__ == "__main__":
    main()