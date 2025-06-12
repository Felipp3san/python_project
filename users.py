# users.py
from data import database

def get_users():
    return database.keys()

def get_user(username):
    if username in get_users():
        return database[username]
    return False

def authenticate():
    username = input("Username: ").strip()
    if get_user(username):
        print(f"Login efetuado como {username}")
        return username 
    else:
        print("Utilizador não encontrado. Registe-se primeiro.")
        return False

def register_user():
    username = input("Novo utilizador: ").strip()
    if get_user(username):
        print("Utilizador já existe. Tente outro.")
    else:
        database[username] = { "tasks": [] }
        print(f"Utilizador '{username}' registado com sucesso.")