# Library System

## Overview
This project is a library system that allows users to add books, borrow books, and find the most borrowed book in the library.

## Features
- **Add Book**: Add a new book to the library.
- **Borrow Book**: Increase the borrow count of a book by 1.
- **Most Borrowed Book**: Find the book with the highest borrow count in the library.

## Structure
The project consists of the following main components:
- **Book Class**: Represents a book with a borrow count.
- **Library Class**: Manages a collection of books.

## Flow
1. **Add Book**: Users can add a book to the library using the `add_book` method of the `Library` class.
2. **Borrow Book**: Users can borrow a book by incrementing its borrow count using the `borrow_book` method of the `Library` class.
3. **Most Borrowed Book**: Users can find the most borrowed book in the library using the `most_borrowed_book` method of the `Library` class.

## Usage
To use the library system:
1. Create an instance of the `Library` class.
2. Add books to the library using the `add_book` method.
3. Borrow books using the `borrow_book` method.
4. Find the most borrowed book using the `most_borrowed_book` method.
