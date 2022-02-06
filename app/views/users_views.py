from app.actions.users_actions import *
from app.actions.books_actions import *


class View:
    def __init__(self):
        self.run = True
        self.user = None

    def main(self):
        self.create_user_or_login()
        if self.run:
            self.library_manager()

    def create_user_or_login(self):
        while self.run:
            self.space()
            print('1-Criar usuário.\n2-Login\n3-Encerrar sessão')
            try:
                op = int(input('Opcao:'))

                if op == 1:
                    payload = self.collect_data_user()
                    if create_user(payload):
                        print('Usuario criado!')
                    else:
                        print('Valores incorretos! Insira uma opcao:')
                elif op == 2:
                    payload = self.collect_data_user()
                else:
                    self.run = False
                    break

                if login(payload):
                    break
                else:
                    print('Usuario invalido! Insira uma opcao:')
            except (ValueError, TypeError):
                print('Valores incorretos! Insira uma opcao:')
                continue

    def library_manager(self):
        while self.run:
            self.space()
            print('\n1-Cadastrar livro.\n2-Atualizar livro\n3-Deletar livro'
                  '\n4-Visualizar livros\n5-Visualizar Usuarios\n6-Encerrar sessão')
            try:
                op = int(input('Opcao:'))

                if op == 1:
                    self.insert_books_view()

                elif op == 2:
                    self.update_books_view()

                elif op == 3:
                    self.delete_books_view()

                elif op == 4:
                    self.space()
                    self.get_books_view()

                elif op == 5:
                    self.space()
                    self.get_users_view()
                else:
                    self.run = False
                    break

            except (ValueError, TypeError, AttributeError):
                print('Valores incorretos! Insira uma opcao:')
                continue

    def insert_books_view(self):
        payload = self.collect_data_book()
        if create_book(payload):
            print(f"'Livro {payload.get('name')} cadastrado!'")
            return True
        print('Nao foi possivel cadastrar!')

    def update_books_view(self):
        book_id = input('Insira o ID(Consulte na opcao 4):')
        data = self.collect_data_book()
        try:
            if data.get('name') and data.get('type'):
                update_book(book_id, name=data.get('name'), _type=data.get('type'), quantity=data.get('quantity'))
                print(f"Livro {data.get('name')} Atualizado!")
            else:
                print('Valores incorretos! Insira uma opcao:')
        except (TypeError, ValueError, AttributeError):
            print('Valores incorretos! Insira uma opcao:')

    @staticmethod
    def get_books_view():
        books = get_books()
        if books:
            for book in books:
                print(f"Id: {book[0]}; Nome: {book[1]}; Tema: {book[2]}; Quantidade: {book[3]}")
        else:
            print('Nao existem livros cadastrados!')

    @staticmethod
    def get_users_view():
        users = get_users()
        if users:
            for user in users:
                print(f"Id: {user[0]}; Email: {user[1]}; Ativo: {user[3]}")
        else:
            print('Nao existem usuarios cadastrados!')

    @staticmethod
    def delete_books_view():
        try:
            book_id = input('Insira o ID(Consulte na opcao 4):')
            if deleted_book(book_id):
                print('Livro Deletado!')
            else:
                print('Livro nao existe, verifique o ID!')
        except (TypeError, ValueError, AttributeError):
            print('Valores incorretos! Insira uma opcao:')

    def collect_data_user(self):
        self.space()
        email = input('E-mail:')
        password = input('Senha:')
        return {'email': email, 'password': password}

    def collect_data_book(self):
        self.space()
        try:
            name = input('Nome:')
            _type = input('Tipo:')
            quantity = int(input('Quantidade:'))
            return {'name': name, 'type': _type, 'quantity': quantity}
        except (ValueError, TypeError, AttributeError):
            pass

    @staticmethod
    def space():
        print('-'*20)
