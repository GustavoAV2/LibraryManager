from typing import Dict, List
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


def update_book(book_id: str, data: Dict) -> Book:
    book: Book = get_book_by_id(book_id)
    list_keys = list(data.keys())

    book.name = data.get('name') if data.get('name') else book.name
    book.type = data.get('type') if data.get('type') else book.type
    book.quantity = data.get('quantity') if data.get('quantity') else book.quantity

    commit()
    return book


def deleted_book(user_id: str) -> Book:
    book: Book = get_book_by_id(user_id)
    delete(book)
    commit()
    return book


def get_books() -> List[Book]:
    books = get(Book)
    return books


def get_book_by_id(book_id: str) -> Book:
    return get_by_column(Book, name_column='id', value_column=book_id)


def get_book_by_name(name: str) -> Book:
    return get_by_column(Book, name_column='name', value_column=name)
