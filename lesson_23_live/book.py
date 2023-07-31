from datetime import date


class BookError(Exception):
    pass


class Book:
    def __init__(self, title, author, book_id):
        self._title = title
        self._author = author
        self._book_id = book_id
        self._is_available = True

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_value):
        if not self._is_available:
            raise Exception("Cannot change title of borrowed book")
        if len(new_value) > 15:
            raise Exception("Name is too long")
        self._title = new_value

    @property
    def author(self):
        return self._author

    @property
    def book_id(self):
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


b1 = Book('Python', "Marius", 1)
print(b1.author)
print(b1.title)
print(b1.book_id)

b1.title = "JAVAJAVAJAVAJAVAJAVAJAVAJAVA"

print(b1.title)

b1.borrow_book()

b1.title = 'C#'


class Reservation:

    def __init__(self, from_date: date, to_date: date):
        self.from_date = from_date
        self.to_date = to_date

    @property
    def duration(self):
        return (self.to_date - self.from_date).days

    def get_duration(self):
        return (self.to_date - self.from_date).days

    def set_duration(self, new_value):
        pass

    @duration.setter
    def duration(self, new_vaue):
        pass


a = Reservation()

a.duration = 12
a.duration

a.get_duration()
a.set_duration(12)


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

    @property
    def has_available_books(self):
        return len(self.list_available_books()) > 0


lib = Library()
lib.has_available_books
