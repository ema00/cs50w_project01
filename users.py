
# Constants for accessing user data in users dictionary
PASSWORD = 0
EMAIL = 1


"""
Dictionary containing user data. Information is stored as:
    key: user ID
    value: list(username, password, email)
Usage: books["0380795272"][TITLE]
"""
users = dict()


"""
Initialization of mock data for users.
"""
def init_users_data():
    users["gonzalezjuan"] = ["gona", "gonzju@hotmail.com"]
    users["perezj"] = ["pejo", "perezjose@hotmail.com"]
    users["gerbaudoari"] = ["arij", "arielger@gmail.com"]
    users["davidm"] = ["davi", "miguens01@gmail.com"]
    users["javito"] = ["jaot", "joter@gmail.com"]


"""
Returns a User object if the username passed as argument corresponds to one of
the users in the users dictionary.
"""
def get_user(username, password):
    if username in users.keys():
        if users[username][PASSWORD] == password:
            return User(username,
                users[username][PASSWORD],
                users[username][EMAIL])
    else:
        return None


"""
Adds the user passed as argument to the users dictionary.
"""
def add_user(user):
    users[user.username] = [user.password, user.email]


"""
Class: User
Represents the data of a user.
"""
class User():

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
