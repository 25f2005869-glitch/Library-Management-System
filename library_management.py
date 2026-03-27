import os

BOOKS_FILE = 'books.txt'

class Library:
    def __init__(self):
        # Load existing books
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, 'r') as f:
                return [line.strip() for line in f.readlines()]
        return []

    def save_books(self):
        with open(BOOKS_FILE, 'w') as f:
            for book in self.books:
                f.write(book + '\n')

    def add_book(self, book_name):
        if not book_name:
            raise ValueError('Book name cannot be empty.')
        # Preventing case-insensitive duplicates
        normalized_name = book_name.lower()
        if normalized_name in (b.lower() for b in self.books):
            raise ValueError('Book already exists.')
        self.books.append(book_name)
        self.save_books()

    def search(self, book_name):
        # Case-insensitive search
        normalized_name = book_name.lower()
        return [book for book in self.books if normalized_name in book.lower()]

    def delete_book(self, book_name):
        normalized_name = book_name.lower()
        self.books = [book for book in self.books if book.lower() != normalized_name]
        self.save_books()