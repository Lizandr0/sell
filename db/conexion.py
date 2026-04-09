import sqlite3

def get_conexion():
    return sqlite3.connect('db/BBDD.db')
    