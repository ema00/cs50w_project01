
# Constants for accessing book data in books dictionary
TITLE = 0
AUTHOR = 1
YEAR = 2


"""
Dictionary containing book data. Information is stored as:
    key: ISBN
    value: list(book name, author, year)
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
Returns a Book object if the ISBN passed as argument corresponds to one of
the books in the books dictionary.
"""
def get_book_by_isbn(isbn):
    if isbn in books.keys():
        return Book(isbn, books[isbn][TITLE],
            books[isbn][AUTHOR],
            books[isbn][YEAR])
    else:
        return None


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
