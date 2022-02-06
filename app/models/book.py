from database import db
from uuid import uuid4


class Book:
    __tablename__ = 'books'

    def __init__(self, name="", _type="", quantity=0):
        self.id = str(uuid4())
        self.name = name
        self.type = _type
        self.quantity = quantity

    def serialize(self):
        return {
                'id': self.name,
                'email': self.type,
                'active': self.quantity
                }

    def __str__(self):
        return f"'{self.id}', '{self.name}', '{self.type}', {self.quantity}"

    def __repr__(self):
        return f"'id', 'name', 'type', 'quantity'"
