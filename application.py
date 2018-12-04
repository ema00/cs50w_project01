import os

from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


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
    # Redirect home, for now...
    return redirect("/")


@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html", message = None)


@app.route("/login", methods=["POST"])
def login_post():
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    if user_credentials_ok(username, password):
        return redirect("/")
    else:
        return render_template("login.html", message="User credentials not valid.")


def user_credentials_ok(username, password):
    return username == "user" and password == "pass"
