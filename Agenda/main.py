from func import *

menu_options: dict = {
    1: 'Fazer login',
    2: 'Criar usuário',
    3: 'Sair',
}
answer = home_menu(menu_options)

match answer:
    case 1:
        create_user()

