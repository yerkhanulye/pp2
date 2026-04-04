import psycopg2
from config import host, port, dbname, user, password


def connect():
    return psycopg2.connect(
        host=host,
        port=port,
        database=dbname,
        user=user,
        password=password
    )