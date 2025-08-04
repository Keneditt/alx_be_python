# library_management.py

class Book:
    """Represents a book with title, author, and checkout status"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track checkout status
    
    @property
    def is_available(self):
        """Public property to check availability"""
        return not self._is_checked_out

class Library:
    """Manages a collection of books with checkout/return functionality"""
    def __init__(self):
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a new book to the library"""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if available"""
        for book in self._books:
            if book.title == title and book.is_available:
                book._is_checked_out = True
                return True
        return False
    
    def return_book(self, title):
        """Return a book by title if checked out"""
        for book in self._books:
            if book.title == title and not book.is_available:
                book._is_checked_out = False
                return True
        return False
    
    def list_available_books(self):
        """List all available books in the library"""
        available_books = [book for book in self._books if book.is_available]
        
        if not available_books:
            print("No available books in the library")
            return
        
        for book in available_books:
            print(f"{book.title} by {book.author}")