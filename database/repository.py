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


def delete(model: object):
    _session.delete(model)
    commit()
    return model


def update(model: object):
    command = f"INSERT INTO {model.__tablename__} ({str(model)})"
    _session.execute(command)
    commit()
    return model


def get(model: object):
    command = f"SELECT * FROM {model.__tablename__} "
    _session.execute(command)
    items = _session.fetchall()
    return items


def get_by_column(model: object, name_column: str, value_column):
    command = f"SELECT * FROM {model.__tablename__} WHERE {name_column}='{value_column}'"
    _session.execute(command)
    item = _session.fetchone()
    return item
