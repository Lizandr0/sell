import sqlite3
from db.conexion import get_conexion
from repositories.repo_meta_mensual import get_meta_mensual, insertar_meta_mensual

conn=get_conexion()
cursor=conn.cursor()

def obtener_meta_mensual():
    try:
        return get_meta_mensual()
    except Exception as e:
        print(f"Error al obtener la meta mensual: {e}")
        return []

def registrar_meta_mensual(nombre, valor, fecha_inicio, fecha_fin):
    try:
        insertar_meta_mensual(cursor, nombre, valor, fecha_inicio, fecha_fin)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error al registrar la meta mensual: {e}")
        return False