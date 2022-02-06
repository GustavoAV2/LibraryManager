from typing import Dict, List, Tuple
from app.models.users import User
from app.models.book import Book
from database.repository import save, update, get, get_by_column, delete, commit


def create_book(data: Dict) -> User or None:
    try:
        return save(Book(
            name=data.get('name'),
            _type=data.get('type'),
            quantity=data.get('quantity')
        ))
    except (AttributeError, KeyError, TypeError):
        return None


def update_book(book_id: str, name: str, _type: str, quantity: int):
    update(Book, f"name='{name}', type='{_type}', quantity='{quantity}'", book_id)


def deleted_book(book_id: str):
    status = True if delete(Book, name_column='id', value_column=book_id).rowcount else False
    return status


def get_books() -> Tuple:
    books = get(Book)
    return books


def get_book_by_id(book_id: str) -> Book:
    return get_by_column(Book, name_column='id', value_column=book_id)


def get_book_by_name(name: str) -> Book:
    return get_by_column(Book, name_column='name', value_column=name)
