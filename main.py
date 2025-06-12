from users import *
from tasks import *

def main():
    while True:
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()
        if menu == 'r':
            register_user()
        elif menu == 'a':
            pass
        elif menu == 'va':
            pass
        elif menu == 'vm':
            pass
        elif menu == 'e':
            exit()
        else:
            print("You have entered an invalid input. Please try again")

main()