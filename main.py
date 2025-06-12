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

        if op == '1':  # Registrar
            username = users.register_user()
            if username:
                print(f"Utilizador '{username}' registado com sucesso.")
            else:
                print("Utilizador já existe. Tente outro.")
        elif op == '2':  # Logar
            user_logged = users.authenticate()
            if user_logged:
                print(f"Login efetuado como {username}")
                user_menu(user_logged)
            else:
                print("Utilizador não encontrado. Registe-se primeiro.")
        elif op == '3':  # Sair
            print("Adeus!")
            break
        else:  # Invalido
            print("Opção inválida. Tente novamente.")
        input("Pressione ENTER para continuar...")


def user_menu(user_logged):
    while True:
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

        if op == '1':
            tasks.add_task(user_logged)
        elif op == '2':
            tasks.edit_task()
        elif op == '3':
            tasks.remove_task()
        elif op == '4':
            # NAO LISTA AS TASKS PENDENTES DE MOMENTO.
            # LISTA TODAS AS TASKS DE UM USER.
            tasks.get_tasks()
        elif op == '5':
            pass
            # mark_as_complete(user)
        elif op == '6':
            tasks.get_tasks_by_user(user_logged)
        elif op == '7':
            pass
            # show_statistics(user)
        elif op == '8':
            print(f"Logout de {user_logged}")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
