import os

from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from books import *
from users import *


init_books_data()
init_users_data()

app = Flask(__name__)

"""
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
"""

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    # Get form information.
    book_data = request.form.get("book")
    # FOR NOW, JUST REDIRECT TO INDEX
    return redirect("/")


@app.route("/book", methods=["GET"])
def book():
    book = get_book_by_isbn("0380795272")
    return render_template("book.html", title = book.title,
        author = book.author, isbn = book.isbn, rating = 3.00,
        rating_good_reads = 5.00, num_revs = 2, num_revs_good_reads = 300)


@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html", message = None)


@app.route("/login", methods=["POST"])
def login_post():
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    user = get_user(username, password)
    if user != None:
        return redirect("/")
    else:
        return render_template("login.html",
            message = "User credentials not valid.")


@app.route("/register", methods=["GET"])
def register_get():
    return render_template("register.html", message = None)


@app.route("/register", methods=["POST"])
def register_post():
    username = str(request.form.get("username"))
    password = str(request.form.get("password1"))
    password_reenter = str(request.form.get("password2"))
    email = str(request.form.get("email"))
    user = get_user(username, password)
    if (password == password_reenter) and (user is None):
        user = User(username, password, email)
        add_user(user)
        return redirect("/")
    else:
        return render_template("register.html", message="User data not valid.")


@app.route("/profile", methods=["GET"])
def profile():
    # FOR NOW, JUST RENDER A MOCK TEMPLATE
    return render_template("profile.html", username = "USER",
        email = "usermail@usermail.com")
