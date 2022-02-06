from database import db

_session = db.cursor()


def commit():
    db.commit()


def save(model: object):
    command = f"INSERT INTO {model.__tablename__} ({model.__repr__()}) VALUES ({str(model)})"
    print(command)
    _session.execute(command)
    commit()
    return model


def delete(model: object, name_column: str, value_column):
    command = f"DELETE FROM {model.__tablename__} WHERE {name_column}='{value_column}'"
    print(command)
    status = _session.execute(command)
    commit()
    return status


def update(model: object, set_columns: str, _id):
    command = f"UPDATE {model.__tablename__} SET {set_columns} WHERE id='{_id}';"
    print(command)
    _session.execute(command)
    commit()
    return model


def get(model: object):
    command = f"SELECT * FROM {model.__tablename__} "
    print(command)
    _session.execute(command)
    items = _session.fetchall()
    return items


def get_by_column(model: object, name_column: str, value_column):
    command = f"SELECT * FROM {model.__tablename__} WHERE {name_column}='{value_column}'"
    print(command)
    _session.execute(command)
    item = _session.fetchone()
    return item
