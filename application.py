import os

from flask import Flask, g, render_template, request, session, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from Book import *
from User import *
from Review import *


# Flask Session key for holding the user ID of the user currently logged in
USER_ID = "user_id"


app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Initialize mock data instead of database, until database is ready
init_books_data()
init_users_data()
init_reviews_data()


"""
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
"""


@app.route("/")
def index():
    if is_user_logged_in():
        return render_template("index.html", books = None)
    else:
        return redirect("/login")


@app.route("/search", methods=["GET", "POST"])
def search():
    if is_user_logged_in():
        book_data = request.form.get("book")
        books = search_books_containing(book_data)
        return render_template("index.html", books = books)
    else:
        return redirect("/login")


@app.route("/book/<string:isbn>", methods=["GET"])
def book(isbn):
    if is_user_logged_in():
        book = get_book_by_isbn(isbn)
        review = get_review_by_book(book)
        return render_template("book.html",
            reviews_br = review.reviews_br,
            book = book, rating = review.rating_br,
            num_revs = review.num_revs_br,
            rating_good_reads = review.review_gr.rating,
            num_revs_good_reads = review.review_gr.num_reviews)
    else:
        return redirect("/login")


@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html", message = None)


@app.route("/login", methods=["POST"])
def login_post():
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    user = get_user(username)
    if not is_user_logged_in():
        if credentials_ok(username, password):
            login(user)
            return redirect("/")
        else:
            return render_template("login.html",
                message = "User credentials not valid.")
    else:
        return redirect("/")


@app.route("/logout", methods=["GET"])
def logout_user():
    logout()
    return redirect("/")


@app.route("/register", methods=["GET"])
def register_get():
    return render_template("register.html", message = None)


@app.route("/register", methods=["POST"])
def register_post():
    username = str(request.form.get("username"))
    password = str(request.form.get("password1"))
    password_reenter = str(request.form.get("password2"))
    email = str(request.form.get("email"))
    user = get_user(username)
    if (password == password_reenter) and (user is None):
        user = User(username, email)
        add_user_and_pass(user, password)
        login(user)
        return redirect("/")
    else:
        return render_template("register.html",
            message="User data not valid.")


@app.route("/profile", methods=["GET"])
def profile():
    if not is_user_logged_in():
        return redirect("/")
    user = get_user(session[USER_ID])
    return render_template("profile.html")


# Helper functions ###########################################################

"""
Loads the user currently logged in. The information is taken from the session
cookie. The global variable g is automatically passed to the template engine.
This is executed before every request.
"""
@app.before_request
def load_logged_in_user():
    user_id = session.get(USER_ID)
    if user_id:
        g.user = get_user(user_id)
    else:
        g.user = None


"""
Logs a user in, using the session cookie.
"""
def login(user):
    session[USER_ID] = user.username


"""
Logs a user out, using the session cookie.
"""
def logout():
    session.clear()


"""
Checks if any user is currently logged in.
"""
def is_user_logged_in():
    return bool(session.get(USER_ID))
