# users.py

from data import users_data

def authenticate():
    username = input("Username: ")

    if username in users_data.keys():
        print("Login válido!")
    else:
        print("Credenciais inválidas.")
    print("You have successfully logged in!")

def register_user():
    while (True):
        new_username = input("To register a user, please enter the username of the new user: ").lower()
        for user in users_data:
            print(user)
            if new_username in user:
                print("The user is already registered.")
            else:
                users_data.append({ new_username: { "tasks": [] } })
                print("New user successfully registered!")
            break