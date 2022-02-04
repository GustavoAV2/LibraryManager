from app.models.book import Book
from app.models.users import User
from database.repository import _session, commit


def create_user_table():
    command = f"CREATE TABLE {User.__tablename__} (email text, password text, active bool)"
    _session.execute(command)
    commit()


def create_book_table():
    command = f"CREATE TABLE {Book.__tablename__} (name text, type text, quantity int)"
    _session.execute(command)
    commit()


if __name__ == '__main__':
    create_user_table()
    create_book_table()
