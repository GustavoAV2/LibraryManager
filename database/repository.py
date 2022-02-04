from database import db

_session = db.cursor()


def commit():
    db.commit()


def save(model: object):
    command = f"INSERT INTO {model.__tablename__} ({str(model)})"
    _session.execute(command)
    commit()
    return model


def delete(model: object):
    _session.delete(model)
    commit()
    return model
