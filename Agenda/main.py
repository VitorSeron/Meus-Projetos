from func import *

menu_options: dict = {
    1: 'Fazer login',
    2: 'Criar usuário',
    0: 'Sair',
}
answer = home_menu(menu_options)

match answer:
    case 1:
        user = str(input('Digite seu usuário: ')).strip()
        password = str(input('Digite sua senha: ')).strip()
        login(user, password)
    case 2:
        create_user()
            

