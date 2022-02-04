from database import db
from uuid import uuid4


class Book:
    __tablename__ = 'books'

    id = str(uuid4())
    name = ""
    type = None
    quantity = 0

    def serialize(self):
        return {
                'id': self.name,
                'email': self.type,
                'active': self.quantity
                }

    def __str__(self):
        return f"'{self.name}', '{self.type}', {self.quantity}"

