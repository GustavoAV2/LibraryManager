from flask import jsonify, request
from typing import Dict, Tuple, Any, List
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from app.actions.users_actions import *
from app.actions.books_actions import *


class View:
    def __init__(self):
        self.run = True
        self.user = None
        self.token = None

    def main(self):
        print('------ BEM VINDO A MARVIN-TECA -------')
        self.create_user_or_login()

        if self.run:
            self.user = get_jwt_identity()
            self.library_manager()

    def create_user_or_login(self):
        while self.run:
            print('1 - Criar usuário.\n2 - Login\n3 - Encerrar sessão')
            try:
                op = int(input('Opcao:'))

                if op == 1:
                    payload = self.collect_user_data()
                    self.user: User = create_user(payload)
                elif op == 2:
                    payload = self.collect_user_data()
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
            print('1 - Cadastrar livro.\n2 - Atualizar livro\n3 - Deletar livro\n4 - Encerrar sessão')
            try:
                op = int(input('Opcao:'))

                if op == 1:
                    self.collect_data_book()

                elif op == 2:
                    self.collect_data_book()

                elif op == 3:
                    self.collect_data_book()

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


if __name__ == '__main__':
    view = View()
    view.main()
