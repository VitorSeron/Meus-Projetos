# Agenda com usuários, CRUD completo
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(
    host='localhost',
    database='agenda-db',
    user='root',
    password='admin',
)
cursor = connection.cursor()

if connection.is_connected():
    print('Conectado ao banco de dados MySQL.')


def connect():

    try:
        connection

    except Error as e:
        print(e)


def create_user():
    name = str(input('Digite seu nome: ')).strip()
    user = str(input('Digite seu usuário para cadastro: ')).strip()
    password = str(input('Digite sua senha para cadastro: ')).strip()
    values = (name, user, password)
    sql = 'INSERT INTO users (name, username, password) VALUES (%s, %s, %s)'
    try:
        cursor.execute(sql, values)
        print('Usuário criado com sucesso.')
        connection.commit()
    except Error as e:
        print('Não foi possível cadastrar.', e)


def login(username, password, name=None):
    values = (username, password)
    sql = 'SELECT * FROM users WHERE username = %s AND password = %s'
    try:
        cursor.execute(sql, values)
        data = cursor.fetchone()
        if data is not None:
            name = data[1]
            user = User(name, username, password)
            print('Logado com sucesso.')
            return user
        else:
            print('Dados incorretos')
        # return data is not None
    except Error as e:
        print('Não foi possível logar.', e)


def home_menu(options: dict) -> int:
    for k, v in options.items():
        print(f'{k} - {v}')
    user_choice = int(input('Digite a opção desejada: '))
    return user_choice


def user_menu(user):
    user_menu_options = {
        1: 'Adicionar novo contato',
        2: 'Ver lista de contatos',
        3: 'Procurar contatos por nome',
        4: 'Procurar contatos por ID',
        5: 'Sair'
    }
    for k, v in user_menu_options.items():
        print(f'{k} - {v}')
    user_choice = int(input('Digite a opção desejada: '))
    return user_choice


class User:
    def __init__(self, name, user, password) -> None:
        self.name = name
        self.user = user
        self.password = password

    def add_contact(self):
        sql = 'INSERT INTO contacts \
            (name, lastname, phone, email, cpf, address) \
            VALUES (%s, %s, %s, %s, %s, %s)'
        name = str(input('Digite o nome do contato: '))
        lastname = str(input(f'Digite o sobrenome de {name}: '))
        phone = str(input(f'Digite o telefone de {name}: '))
        email = str(input(f'Digite o e-mail de {name}: '))
        cpf = str(input(f'Digite o cpf de {name}: '))
        address = str(input(f'Digite o endereço de {name}: '))
        values = (name, lastname, phone, email, cpf, address)
        try:
            cursor.execute(sql, values)
            connection.commit()
            print('Contato cadastrado com sucesso.')
        except Error as e:
            print(f'Não foi possível cadastrar o contato {name}.', e)

    def list_contacts(self):
        sql = 'SELECT * FROM contacts'
        try:
            cursor.execute(sql)
            contacts = cursor.fetchall()
            for contact in contacts:
                print(contact)
        except Error as e:
            print('Não foi possível listar os contatos.', e)

    def search_by_name(self):
        name = str(input('Digite o nome ou sobrenome a ser buscado: '))
        sql = f"SELECT * FROM contacts c WHERE name LIKE '%{name}%'"
        try:
            cursor.execute(sql, name)
            print('Resultado da busca: ')
            contacts = cursor.fetchall()
            for contact in contacts:
                print(contact)
        except Error as e:
            print(f'Não foi possível localizar {name}.')

    def search_by_id(self):
        ...


if __name__ == "__main__":
    connect()
    user = User('Vitor', 'Trinho182', 'trinho182')
    user.list_contacts()
    print('Fim')
