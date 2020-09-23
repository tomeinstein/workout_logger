import sqlite3
from flask import g, current_app

DATABASE = "workout_logger.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = make_dicts
    return db

def query_db(query, args=(), commit=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    print(rv)
    cur.close()
    if commit:
        get_db().commit()
    return rv

def init_db():
    db = sqlite3.connect(DATABASE)
    with open('api/resources/schema.sql') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def close_db(e=None):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()