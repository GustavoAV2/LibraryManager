from flask_jwt_extended import (jwt_required, get_jwt_identity)
from app.actions.users_actions import *
from app.actions.books_actions import *


class View:
    def __init__(self):
        self.run = True
        self.user = None
        self.token = None

    def main(self):
        self.create_user_or_login()

        if self.run:
            self.library_manager()

    def create_user_or_login(self):
        while self.run:
            print('-'*20 + '\n1 - Criar usuário.\n2 - Login\n3 - Encerrar sessão')
            try:
                op = int(input('Opcao:'))

                if op == 1:
                    payload = self.collect_data_user()
                    self.user: User = create_user(payload)
                elif op == 2:
                    payload = self.collect_data_user()
                else:
                    self.run = False
                    break

                self.token = login(payload)
                if self.token:
                    break
                else:
                    print('Não foi possível criar usuário! Insira uma opcao:')
            except (ValueError, TypeError):
                print('Valor incorreto! Insira uma opcao:')
                continue

    def library_manager(self):
        while self.run:
            self.space()
            print('\n1-Cadastrar livro.\n2-Atualizar livro\n3-Visualizar livros\n4-Deletar livro\n5-Encerrar sessão')
            try:
                op = int(input('Opcao:'))

                if op == 1:
                    payload = self.collect_data_book()
                    create_book(payload)
                elif op == 2:
                    payload = self.collect_data_book()
                    # update_book(payload)
                elif op == 3:
                    self.space()
                    books = get_books()
                    if books:
                        for book in books:
                            print(book)
                    else:
                        print('Nao existem livros cadastrados!')
                elif op == 4:
                    payload = self.collect_data_book()
                    # deleted_book(payload)
                else:
                    self.run = False
                    break

            except (ValueError, TypeError):
                print('Valor incorreto! Insira uma opcao:')
                continue

    @staticmethod
    def collect_data_user():
        email = input('E-mail:')
        password = input('Senha:')
        return {'email': email, 'password': password}

    @staticmethod
    def collect_data_book():
        name = input('Nome:')
        _type = input('Tipo:')
        quantity = input('Quantidade:')
        return {'name': name, 'type': _type, 'quantity': quantity}

    @staticmethod
    def space():
        print('-'*20)

if __name__ == '__main__':
    view = View()
    view.main()
