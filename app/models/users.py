from uuid import uuid4
from werkzeug.security import check_password_hash


class User:
    __tablename__ = 'users'

    def __init__(self, email="", password="", active=True):
        self.id = str(uuid4())
        self.email = email
        self.password = password
        self.active = active

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def serialize(self):
        return {
                'id': self.id,
                'email': self.email,
                'active': self.active
                }

    def __str__(self):
        return f"'{self.id}', '{self.email}', '{self.password}', {self.active}"

    def __repr__(self):
        return f"'id', 'email', 'password', 'active'"
