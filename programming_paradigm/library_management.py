class Book:
    """Represents a book with title, author, and checkout status"""
    
    def __init__(self, title, author):
        """
        Initialize a Book instance
        
        :param title: Title of the book
        :param author: Author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track checkout status
    
    def check_out(self):
        """Mark the book as checked out"""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned/available"""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books with checkout/return functionality"""
    
    def __init__(self):
        """Initialize a Library with empty book list"""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a book to the library"""
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by title
        
        :param title: Title of the book to check out
        :return: True if successful, False if book not found or already checked out
        """
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return True
                else:
                    return False  # Book is already checked out
        return False  # Book not found
    
    def return_book(self, title):
        """
        Return a book by title
        
        :param title: Title of the book to return
        :return: True if successful, False if book not found or not checked out
        """
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return True
                else:
                    return False  # Book was not checked out
        return False  # Book not found
    
    def list_available_books(self):
        """List all available books in the library"""
        available_books = [book for book in self._books if book.is_available()]
        
        for book in available_books:
            print(book)