from typing import Dict,  Tuple
from app.models.users import User
from werkzeug.security import generate_password_hash
from database.repository import save, delete, get, get_by_column, update


def login(data: Dict) -> bool:
    try:
        payload = get_user_by_email(data.get('email'))

        if not payload[3]:
            return False

        user = User(payload[1], payload[2], True)
        if not user or not user.verify_password(data.get('password')):
            return False

        return True
    except (AttributeError, KeyError, TypeError):
        return False


def create_user(data: Dict) -> User or None:
    try:
        if data.get('email') and data.get('password'):
            return True if save(User(
                email=data.get('email'),
                password=generate_password_hash(data.get('password'))
            )).rowcount else False
    except (AttributeError, KeyError, TypeError):
        return None


def update_user(user_id: str, email="", password="", active=True):
    update(User, f"email='{email}', password='{password}', active='{active}'", user_id)


def deleted_user(user_id: str):
    delete(User, name_column='id', value_column=user_id)


def get_users() -> Tuple:
    users = get(User)
    return users


def get_user_by_id(user_id: str) -> User:
    return get_by_column(User, name_column='id', value_column=user_id)


def get_user_by_email(email: str) -> []:
    return get_by_column(User, name_column='email', value_column=email)
