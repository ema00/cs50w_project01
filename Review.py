
import datetime
import json


# Minimum possible value of a review (number of stars) for Book Review web
REVIEW_MIN = 0
# Maximum possible value for a review (number of stars) for Book Review web
REVIEW_MAX = 5

# Constants for accessing book reviews data in Book Review dictionary
# These are for accesing review of a book for a given user
REVIEW = 0
DATE = 1


"""
Dictionary containing book reviews data from Book Review webpage. Information
is stored as:
    key: ISBN
    value: dict(username, [review, datetime])
Usage: reviews_bookreview["0380795272"]
"""
reviews_bookreview = dict()


"""
Dictionary containing book reviews data from Goodreads webpage. Information
is stored as:
    key: ISBN
    value: JSON object
Usage: reviews_goodreads["0380795272"]
"""
reviews_goodreads = dict()


"""
Initialization of mock data for reviews. This just calls the initialization
functions for the mock data of Book Review webpage and Goodreads webpage.
"""
def init_reviews_data():
    # Init mock data for reviews data from Book Review webpage
    init_reviews_br_data()
    # Init mock data for reviews data from Goodreads webpage
    init_reviews_gr_data()


"""
Returns a Review object for the Book passed as argument, if the Book has a
review in the reviews dictionaries.
"""
def get_review_by_book(book):
    isbn = book.isbn
    return get_review_by_isbn(isbn)


"""
Returns a Review object for the Book whose ISBN is passed as argument, if the
Book has a review in the reviews dictionaries.
"""
def get_review_by_isbn(isbn):
    if isbn in reviews_bookreview.keys():
        review_br = reviews_bookreview[isbn]
    else:
        review_br = None
    if book.isbn in reviews_goodreads.keys():
        review_gr = reviews_goodreads[isbn]
    else:
        review_gr = None
    return Review(book, review_br, review_gr)


"""
Adds a review for a Book, by a specific User, to the dictionary thet contains
reviews for Book Review website.
Does not add the review if the book has already been added by the user.
Does not add the review if the book or the user are None.
"""
def add_br_review(book, user, review):
    username = user.username
    isbn = book.isbn
    if book is None or user is None:
        return
    if username in reviews_bookreview[book.isbn].keys():
        return
    if review < REVIEW_MIN:
        review = REVIEW_MIN
    elif review > REVIEW_MAX:
        review = REVIEW_MAX
    if isbn not in reviews_bookreview:
        reviews_bookreview[isbn] = dict()
    reviews_bookreview[isbn][username] = [review, datetime.datetime.now()]


"""
Class: Review
Represents the reviews of a Book, from both Book Review and Goodreads.
"""
class Review():

    def __init__(self, book, review_br, review_gr):
        self.book = book
        # Review from Book Review
        self. = review_br
        # Review from Goodreads
        self.review_gr = review_gr

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, book):
        self.__book = book

    @property
    def review_br(self):
        return self.__review_br

    @review_br.setter
    def review_br(self, review_br):
        if review_br is None:
            self.__review_br = { self.book : list() }
        else:
            self.__review_br = review_br

    @property
    def review_gr(self):
        return self.__review_gr

    @review_gr.setter
    def review_gr(self, review_gr):
        if __review_gr is None:
            self.__review_gr = { self.book : dict() }
        else:
            self.__review_gr = review_gr


"""
Initialization of mock data for reviews from Book Review webpage.
"""
def init_reviews_br_data():
    reviews_bookreview["0380795272"] = {
        "gonzalezjuan" : [2, datetime.datetime(2018, 6, 2, 23, 30, 14)],
        "davidm" : [4, datetime.datetime(2010, 11, 4, 21, 12, 6)]
    }
    reviews_bookreview["1416949658"] = {
        "javito" : [4, datetime.datetime(2011, 4, 15, 21, 12, 34)],
        "gerbaudoari" : [3, datetime.datetime(2012, 3, 14, 1, 2, 4)]
    }
    reviews_bookreview["1857231082"] = {
        "gerbaudoari" : [3, datetime.datetime(2011, 4, 15, 21, 12, 34)],
        "davidm" : [3, datetime.datetime(2010, 11, 4, 21, 12, 6)]
    }
    reviews_bookreview["0553803700"] = {
        "gonzalezjuan" : [5, datetime.datetime(2017, 4, 14, 21, 12, 6)],
        "gerbaudoari" : [5, datetime.datetime(2018, 2, 5, 23, 30, 14)]
    }
    reviews_bookreview["080213825X"] = dict()
    reviews_bookreview["0375913750"] = dict()
    reviews_bookreview["074349671X"] = dict()
    reviews_bookreview["0743454553"] = dict()
    reviews_bookreview["0765317508"] = {
        "gerbaudoari" : [1, datetime.datetime(2015, 12, 6, 2, 4, 14)],
    }
    reviews_bookreview["0142501085"] = {
        "gonzalezjuan" : [2, ],
    }
    reviews_bookreview["1442468351"] = {
        "davidm" : [3, datetime.datetime(2014, 2, 4, 12, 6, 4)]
    }
    reviews_bookreview["1439152802"] = {
        "javito" : [2, datetime.datetime(2018, 12, 24, 2, 16, 40)],
        "gerbaudoari" : [1, datetime.datetime(2016, 5, 6, 7, 20, 4)]
    }
    reviews_bookreview["0399153942"] = {
        "davidm" : [4, datetime.datetime(2018, 12, 24, 2, 16, 40)]
    }
    reviews_bookreview["0441017835"] = dict()


"""
Initialization of mock data for reviews from Goodreads webpage.
"""
def init_reviews_gr_data():
    reviews_goodreads["0380795272"] =
"""
{
    "title": "Krondor: The Betrayal",
    "author": "Raymond E. Feist",
    "year": 1998,
    "isbn": "0380795272",
    "review_count": 28,
    "average_score": 4.3
}
"""
    reviews_goodreads["1416949658"] =
"""
{
    "title": "The Dark Is Rising",
    "author": "Susan Cooper",
    "year": 1973,
    "isbn": "1416949658",
    "review_count": 34,
    "average_score": 3.8
}
    """
    reviews_goodreads["1857231082"] =
"""
{
    "title": "The Black Unicorn",
    "author": "Terry Brooks",
    "year": 1987,
    "isbn": "1857231082",
    "review_count": 25,
    "average_score": 4.1
}
"""
    reviews_goodreads["0553803700"] =
"""
{
    "title": "I, Robot",
    "author": "Isaac Asimov",
    "year": 1950,
    "isbn": "0553803700",
    "review_count": 90,
    "average_score": 4.8
}
"""
    reviews_goodreads["080213825X"] =
"""
{
    "title": "Four Blondes",
    "author": "Candace Bushnell",
    "year": 2000,
    "isbn": "080213825X",
    "review_count": 92,
    "average_score": 3.7
}
"""
    reviews_goodreads["0375913750"] =
"""
{
    "title": "Love, Stargirl",
    "author": "Jerry Spinelli",
    "year": 2007,
    "isbn": "0375913750",
    "review_count": 90,
    "average_score": 4.8
}
"""
    reviews_goodreads["074349671X"] =
"""
{
    "title": "The Tenth Circle",
    "author": "Jodi Picoult"",
    "year": 2006,
    "isbn": "074349671X",
    "review_count": 13,
    "average_score": 2.8
}
"""
    reviews_goodreads["0743454553"] =
"""
{
    "title": "Vanishing Acts",
    "author": "Jodi Picoult",
    "year": 2005,
    "isbn": "0743454553",
    "review_count": 10,
    "average_score": 3.3
}
"""
    reviews_goodreads["0765317508"] =
"""
{
    "title": "Aztec",
    "author": "Gary Jennings",
    "year": 1980,
    "isbn": "0765317508",
    "review_count": 39,
    "average_score": 3.8
}
"""
    reviews_goodreads["0142501085"] =
"""
{
    "title": "Marlfox",
    "author": "Brian Jacques",
    "year": 1998,
    "isbn": "0142501085",
    "review_count": 37,
    "average_score": 4.1
}
"""
    reviews_goodreads["1442468351"] =
"""
{
    "title": "Lady Midnight",
    "author": "Cassandra Clare",
    "year": 2016,
    "isbn": "1442468351",
    "review_count": 80,
    "average_score": 4.1
}
"""
    reviews_goodreads["1439152802"] =
"""
{
    "title": "The Secret Keeper",
    "author": "Kate Morton",
    "year": 2012,
    "isbn": "1439152802",
    "review_count": 30,
    "average_score": 4.2
}
"""
    reviews_goodreads["0399153942"] =
"""
{
    "title": "The Afghan",
    "author": "Frederick Forsyth",
    "year": 2006,
    "isbn": "0399153942",
    "review_count": 50,
    "average_score": 4.1
}
"""
    reviews_goodreads["0441017835"] =
"""
{
    "title": "A Touch of Dead",
    "author": "Charlaine Harris",
    "year": 2009,
    "isbn": "0441017835",
    "review_count": 20,
    "average_score": 4.0
}
"""

    # convert Goodreads reviews to JSON
    for isbn in reviews_goodreads.keys():
        reviews_goodreads[isbn] = json.loads(reviews_goodreads[isbn])
