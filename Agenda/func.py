# Agenda com usuários, CRUD completo
import json


def create_user() -> dict:
    user = str(input('Digite um usuário para cadastro: ')).strip()
    password = str(input('Digite uma senha para cadastro: ')).strip()
    login_input: dict = {user: password}
    with open('users_db.json', 'w+', encoding='utf8') as arquivo:
        try:
            json.dump( login_input ,arquivo, indent=2, ensure_ascii=False)
        except Exception:
            print('Não foi possível cadastrar')
    return login_input



def login(user, password):
    user = str(input('Digite seu usuário: ')).strip()
    password = str(input('Digite sua senha: ')).strip()
    with open('users_db.json', 'r', encoding='utf8'):
        try:
            ...
        except:
            ...
        finally:
            ...
    return User(user)


def home_menu(options: dict) -> int:
    for k, v in options.items():
        print(f'{k} - {v}')
    user_choice = int(input('Digite a opção desejada: '))
    return user_choice


class User:
    def __init__(self, user, password, email, phone) -> None:
        self.user = user
        self.password = password

    def login(user, password):
        ...
