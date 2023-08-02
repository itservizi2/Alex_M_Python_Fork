# Notite:

Private inseamna cu _underscore

Exemplu: `_account_number` - (astfel nu permitem sa accesam direct fieldul)

## Banking System (OOP) in Python:

1. Create a class called `BankAccount`.
    - Properties:
        - account_number (private)
        - account_holder_name (private)
        - balance (private)

    - Methods:
        - `__init__(account_number, account_holder_name)`: Constructor to initialize account number, account holder
          name, and set balance to 0.
        - `get_account_number()`: Get the account number.
        - `get_account_holder_name()`: Get the account holder name.
        - `get_balance()`: Get the account balance.
        - `deposit(amount)`: Deposit money into the account.
        - `withdraw(amount)`: Withdraw money from the account.

2. Create a subclass called `SavingsAccount`, which extends `BankAccount`.
    - Additional Property:
        - interest_rate (private)

    - Methods (Overrides):
        - `__init__(account_number, account_holder_name, interest_rate)`: Constructor to initialize the interest rate
          for savings accounts.

3. Create a subclass called `CurrentAccount`, which also extends `BankAccount`.
    - Additional Property:
        - overdraft_limit (private)

    - Methods (Overrides):
        - `__init__(account_number, account_holder_name, overdraft_limit)`: Constructor to initialize the overdraft
          limit for current accounts.

## Library Management System (OOP) in Python:

1. Create a class called `Book`.
    - Properties:
        - title
        - author
        - book_id (private)
        - is_available (private)

    - Methods:
        - `__init__(title, author, book_id)`: Constructor to initialize book title, author, and generate a unique book
          ID. Set availability to True.
        - `get_title()`: Get the title of the book.
        - `get_author()`: Get the author of the book.
        - `get_book_id()`: Get the book ID.
        - `is_book_available()`: Check if the book is available for borrowing.
        - `borrow_book()`: Borrow the book (set availability to False).
        - `return_book()`: Return the book (set availability to True).

2. Create a class called `Library`.
    - Properties:
        - name
        - location
        - books (private list of Book objects)

    - Methods:
        - `__init__(name, location)`: Constructor to initialize the library's name, location, and an empty list for
          books.
        - `add_book(book)`: Add a book to the library's collection.
        - `remove_book(book_id)`: Remove a book from the library's collection based on its ID.
        - `search_book(title)`: Search for a book in the library by title.
        - `list_available_books()`: List all available books in the library.

# Testing

For both the tasks above, create functions that check if the functionality works well.

# RO

## Sistem Bancar (OOP) în Python:

1. Creați o clasă numită `BankAccount` (Cont Bancar).
    - Proprietăți:
        - account_number (număr de cont) (privat)
        - account_holder_name (nume deținător de cont) (privat)
        - balance (sold) (privat)

    - Metode:
        - `__init__(account_number, account_holder_name)`: Constructor pentru a inițializa numărul de cont, numele
          deținătorului de cont și a seta soldul la 0.
        - `get_account_number()`: Obțineți numărul de cont.
        - `get_account_holder_name()`: Obțineți numele deținătorului de cont.
        - `get_balance()`: Obțineți soldul contului.
        - `deposit(amount)`: Depuneți bani în cont.
        - `withdraw(amount)`: Retrageți bani din cont.

2. Creați o subclasă numită `SavingsAccount` (Cont de Economii), care extinde clasa `BankAccount` (Cont Bancar).
    - Proprietate suplimentară:
        - interest_rate (rată dobândă) (privat)

    - Metode (Suprascrieri):
        - `__init__(account_number, account_holder_name, interest_rate)`: Constructor pentru a inițializa rata dobânzii
          pentru conturile de economii.

3. Creați o subclasă numită `CurrentAccount` (Cont Curent), care de asemenea extinde clasa `BankAccount` (Cont Bancar).
    - Proprietate suplimentară:
        - overdraft_limit (limită de descoperire) (privat)

    - Metode (Suprascrieri):
        - `__init__(account_number, account_holder_name, overdraft_limit)`: Constructor pentru a inițializa limita de
          descoperire pentru conturile curente.

## Sistem de Management al Bibliotecii (OOP) în Python:

1. Creați o clasă numită `Book` (Carte).
    - Proprietăți:
        - title (titlu)
        - author (autor)
        - book_id (ID carte) (privat)
        - is_available (disponibilă) (privat)

    - Metode:
        - `__init__(title, author, book_id)`: Constructor pentru a inițializa titlul cărții, autorul și pentru a
          genera un ID unic pentru carte. Setează disponibilitatea la True.
        - `get_title()`: Obțineți titlul cărții.
        - `get_author()`: Obțineți autorul cărții.
        - `get_book_id()`: Obțineți ID-ul cărții.
        - `is_book_available()`: Verificați dacă cartea este disponibilă pentru împrumut.
        - `borrow_book()`: Împrumutați cartea (setează disponibilitatea la False).
        - `return_book()`: Returnați cartea (setează disponibilitatea la True).

2. Creați o clasă numită `Library` (Bibliotecă).
    - Proprietăți:
        - name (nume)
        - location (locatie)
        - books (cărți) (listă privată de obiecte Book)

    - Metode:
        - `__init__(name, location)`: Constructor pentru a inițializa numele bibliotecii, locația și o listă goală
          pentru
          cărți.
        - `add_book(book)`: Adăugați o carte în colecția bibliotecii.
        - `remove_book(book_id)`: Eliminați o carte din colecția bibliotecii bazat pe ID-ul său.
        - `search_book(title)`: Căutați o carte în bibliotecă după titlu.
        - `list_available_books()`: Listați toate cărțile disponibile în bibliotecă.

# Testare

Pentru ambele sarcini de mai sus, creați funcții care verifică dacă funcționalitatea funcționează corect.