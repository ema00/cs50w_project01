
# Constants for accessing user data in users dictionary
EMAIL = 0


"""
Dictionary containing users data. This is the current users data store until
the DB data store is implemented.
Information is stored as:
    key: username
    value: list(email)
Usage: email = users["0380795272"][EMAIL]
"""
users = dict()

"""
Dictionary containing users passwords. This is the current passwords data
store until the DB data store is implemented.
Information is stored as:
    key: user ID
    value: password
Usage: password = passwords["0380795272"]
"""
passwords = dict()


"""
Initialization of mock data for users. This simulates the data stored in a DB.
These are the current users and passwords data stores until the DB data store
is implemented.
"""
def init_users_data():
    # Init users data
    users["gonzalezjuan"] = ["gonzju@hotmail.com"]
    users["perezj"] = ["perezjose@hotmail.com"]
    users["gerbaudoari"] = ["arielger@gmail.com"]
    users["davidm"] = ["miguens01@gmail.com"]
    users["javito"] = ["joter@gmail.com"]
    # Init users passwords
    passwords["gonzalezjuan"] = "gona"
    passwords["perezj"] = "pejo"
    passwords["gerbaudoari"] = "arij"
    passwords["davidm"] = "davi"
    passwords["javito"] = "jaot"


"""
Returns true if user and password are OK for the user.
"""
def credentials_ok(username, password):
    return (username in users.keys()) and (passwords[username] == password)


"""
Returns a User object if the username passed as argument corresponds to one of
the users in the users data store.
"""
def get_user(username):
    if username in users.keys():
        return User(username, users[username][EMAIL])
    else:
        return None


"""
Adds the user passed as argument to the users data store.
Also adds the password to the user.
"""
def add_user_and_pass(user, password):
    users[user.username] = [user.email]
    passwords[user.username] = password


"""
Class: User
Represents the data of a user.
"""
class User():

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
