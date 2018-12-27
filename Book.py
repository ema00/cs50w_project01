
# Constants for accessing book data in books dictionary
TITLE = 0
AUTHOR = 1
YEAR = 2


"""
Dictionary containing book data. Information is stored as:
    key: ISBN
    value: list(title, author, year)
Usage: books["0380795272"][TITLE]
"""
books = dict()


"""
Initialization of mock data for users and books.
"""
def init_books_data():
    books["0380795272"] = ["Krondor: The Betrayal", "Raymond E. Feist", 1998]
    books["1416949658"] = ["The Dark Is Rising", "Susan Cooper", 1973]
    books["1857231082"] = ["The Black Unicorn", "Terry Brooks", 1987]
    books["0553803700"] = ["I, Robot", "Isaac Asimov", 1950]
    books["080213825X"] = ["Four Blondes", "Candace Bushnell", 2000]
    books["0375913750"] = ["Love, Stargirl", "Jerry Spinelli", 2007]
    books["074349671X"] = ["The Tenth Circle", "Jodi Picoult", 2006]
    books["0743454553"] = ["Vanishing Acts", "Jodi Picoult", 2005]
    books["0765317508"] = ["Aztec", "Gary Jennings", 1980]
    books["0142501085"] = ["Marlfox", "Brian Jacques", 1998]
    books["1442468351"] = ["Lady Midnight", "Cassandra Clare", 2016]
    books["1439152802"] = ["The Secret Keeper", "Kate Morton", 2012]
    books["0399153942"] = ["The Afghan", "Frederick Forsyth", 2006]
    books["0441017835"] = ["A Touch of Dead", "Charlaine Harris", 2009]


"""
Returns a Book object if the ISBN passed as argument corresponds to one of the
books in the books dictionary.
"""
def get_book_by_isbn(isbn):
    if isbn in books.keys():
        return Book(isbn, books[isbn][TITLE],
            books[isbn][AUTHOR],
            books[isbn][YEAR])
    else:
        return None


"""
Returns a Set of Book objects that contain the "string" parameter in the ISBN,
author or title.
First removes whitespace characters from beginning and end, then searches the
books by the string argument, and then returns a set of Book instences
matching the result.
"""
def search_books_containing(string):
    result = set()
    if string is None:
        return result
    string = string.lstrip().rstrip().lower()
    if string == "":
        return result
    for isbn in books.keys():
        if book_contains(isbn, string):
            title = books[isbn][TITLE]
            author = books[isbn][AUTHOR]
            year = books[isbn][YEAR]
            book = Book(isbn, title, author, year)
            result.add(book)
    return result


"""
Returns True if the string passed as argument is in the book whose isbn is,
passed as argument. The search is performed in the isbn, in the name, and in
the author of the book passed as argument. Returns False if the string is not
found in any of the three.
"""
def book_contains(isbn, string):
    return isbn.find(string) != -1 or \
        books[isbn][TITLE].lower().find(string) != -1 or \
        books[isbn][AUTHOR].lower().find(string) != -1


"""
Class: Book
Represents the data of a Book.
"""
class Book():

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year
