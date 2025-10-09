class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Book: {self.title} by {self.author}, ISBN: {self.isbn}"

    def __repr__(self):
        return f"Book(\'{self.title}\', \'{self.author}\', \'{self.isbn}\')"

class EBook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, ISBN: {self.isbn}, File Size: {self.file_size}MB"

    def __repr__(self):
        return f"EBook(\'{self.title}\', \'{self.author}\', \'{self.isbn}\', {self.file_size})"

class PrintBook(Book):
    def __init__(self, title, author, isbn, page_count):
        super().__init__(title, author, isbn)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, ISBN: {self.isbn}, Pages: {self.page_count}"

    def __repr__(self):
        return f"PrintBook(\'{self.title}\', \'{self.author}\', \'{self.isbn}\', {self.page_count})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added \'{book.title}\' to the library.")
        else:
            print("Invalid book object provided.")

    def remove_book(self, isbn):
        initial_len = len(self.books)
        self.books = [book for book in self.books if book.isbn != isbn]
        if len(self.books) < initial_len:
            print(f"Book with ISBN {isbn} removed from the library.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

    def find_book(self, search_term):
        found_books = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or \
               search_term.lower() in book.author.lower() or \
               search_term == book.isbn:
                found_books.append(book)
        return found_books

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)