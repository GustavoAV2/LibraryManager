from uuid import uuid4
from werkzeug.security import check_password_hash


class User:
    __tablename__ = 'users'

    id = str(uuid4())
    email = ""
    password = None
    active = True

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def serialize(self):
        return {
                'id': self.id,
                'email': self.email,
                'active': self.active
                }
