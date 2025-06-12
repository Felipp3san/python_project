# main.py

import os
import users
import tasks


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    user_logged = None

    while True:
        clear_terminal()
        print("\n--- MENU PRINCIPAL ---")
        print("1. Registar utilizador")
        print("2. Login")
        print("3. Sair")
        op = input("Escolha uma opção: ")

        # REGISTER
        if op == '1':
            username = input("Novo utilizador: ").strip()
            if users.register_user(username):
                print(f"Utilizador '{username}' registado com sucesso.")
            else:
                print("Utilizador já existe. Tente outro.")
        # LOGIN
        elif op == '2':
            username = input("Username: ").strip()
            if users.authenticate(username):
                user_logged = username
                print(f"Login efetuado como {user_logged}")
                user_menu(user_logged)
            else:
                print("Utilizador não encontrado. Registe-se primeiro.")
        # QUIT
        elif op == '3':
            print("Adeus!")
            break
        # INVALID
        else:
            print("Opção inválida. Tente novamente.")
        input("Pressione ENTER para continuar...")


def user_menu(user_logged):
    while True:
        clear_terminal()
        print(f"\n--- MENU {user_logged} ---")
        print("1. Adicionar tarefa")
        print("2. Editar tarefa")
        print("3. Remover tarefa")
        print("4. Listar tarefas pendentes")
        print("5. Marcar tarefa como concluída")
        print("6. Pesquisar tarefas")
        print("7. Ver estatísticas")
        print("8. Logout")
        op = input("Escolha uma opção: ")

        # ADD TASK
        if op == '1':
            tasks.add_task(user_logged)
        # EDIT TASK
        elif op == '2':
            tasks.edit_task()
        # REMOVE TASK
        elif op == '3':
            tasks.remove_task()
        # GET PENDING TASKS
        elif op == '4':
            # NAO LISTA AS TASKS PENDENTES DE MOMENTO.
            # LISTA TODAS AS TASKS DE UM USER.
            tasks.get_tasks()
        # MARK AS COMPLETE
        elif op == '5':
            pass
            # mark_as_complete(user)
        # SEARCH TASKS
        elif op == '6':
            tasks.get_tasks_by_user(user_logged)
        # SHOW STATISTICS
        elif op == '7':
            pass
            # show_statistics(user)
        # LOGOUT
        elif op == '8':
            print(f"Logout de {user_logged}")
            break
        # INVALID
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
