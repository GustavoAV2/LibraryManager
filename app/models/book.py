from database import db
from uuid import uuid4


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    name = db.Column(db.String(84), nullable=False, unique=True)
    type = db.Column(db.String(128), nullable=True)
    quantity = db.Column(db.Integer(), default=True)

    def serialize(self):
        return {
                'id': self.name,
                'email': self.type,
                'active': self.quantity
                }
