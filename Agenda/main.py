from func import *

connect()

menu_options: dict = {
    1: 'Criar usuário',
    2: 'Fazer login',
    0: 'Sair',
}
answer = home_menu(menu_options)

match answer:
    case 1:
        create_user()
    case 2:
        username = str(input('Digite seu username: '))
        password = str(input('Digite sua senha: '))
        user = login(username, password)
        if user:
            print(f'Bem vindo {user.name}')
            while True:
                answer = user_menu(user)
                match answer:
                    case 1:
                        user.add_contact()
                    case 2:
                        user.list_contacts()
                    case 3:
                        user.search_by_name()
                    case 4:
                        user.search_by_id()
                    case 5:
                        print('Saindo do programa')
                        break
                    case _:
                        print('Opção inválida')
        else:
            print('Usuário não logado')
    case 0:
        print('Saindo do programa.')
    case _:
        print('Opção inválida.')
