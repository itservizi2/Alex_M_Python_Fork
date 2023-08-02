class BookError(Exception):
    pass


class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self._book_id = book_id
        self._is_available = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_book_id(self):
        return self._book_id

    def is_book_available(self):
        return self._is_available

    def borrow_book(self):
        if not self._is_available:
            raise BookError("Book is already borrowed")
        self._is_available = False

    def return_book(self):
        if self._is_available:
            raise BookError("Book is already in library")
        self._is_available = True


class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book_id):
        for book in self._books:
            if book.get_book_id() == book_id:
                self._books.remove(book)
                return
        raise BookError("Book not found")

    def search_book(self, title):
        for book in self._books:
            if book.get_title() == title:
                return book
        raise BookError("Book not found")

    def list_available_books(self):
        available_books = []
        for book in self._books:
            if book.is_book_available():
                available_books.append(book)
        return available_books


# Generam careva carti
book1 = Book("Aventurile lui Tom Sawyer", "Mark Twain", 1)
book2 = Book("Amintiri din copilarie", "Ion Creanga", 2)

# Cream biblioteca
library = Library("Biblioteca scolarului", "Sector Centru")

# Adaugam carti in biblioteca
library.add_book(book1)
library.add_book(book2)


def test_add_book():
    print("Testing add_book()")
    try:
        library.add_book(Book("Poezii", "Mihai Eminescu", 3))
        print(library._books)
        if len(library._books) == 3:
            print("add_book test passed")
        else:
            print("add_book test failed")
    except BookError as e:
        print("Test failed:", e)


def test_remove_book():
    print("Testing remove_book()")
    try:
        library.remove_book(2)
        if len(library._books) == 2:
            print("remove_book test passed")
        else:
            print("remove_book test failed")
    except BookError as e:
        print("Test failed:", e)


def test_search_book():
    print("Testing search_book()")
    try:
        book = library.search_book("Poezii")
        if book.title == "Poezii":
            print("search_book test passed")
        else:
            print("search_book test failed")
    except BookError as e:
        print("Test failed:", e)


def test_list_available_books():
    print("Testing list_available_books()")
    try:
        books = library.list_available_books()
        if len(books) == 2 and books[0].title == "Poezii":
            print("list_available_books test passed")
        else:
            print("list_available_books test failed")
    except BookError as e:
        print("Test failed:", e)


test_add_book()
test_remove_book()
test_search_book()
test_list_available_books()

