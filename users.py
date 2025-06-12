# users.py

from data import database


def get_users():
    return database.keys()


def get_user(username):
    if username in get_users():
        return database[username]
    return False


def authenticate(username):
    return get_user(username)


def register_user(username):
    if not get_user(username):
        database[username] = {"tasks": []}
        return username
    else:
        return False
