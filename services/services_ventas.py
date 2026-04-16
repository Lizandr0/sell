import sqlite3
from db.conexion import get_conexion
from repositories.repo_ventas import get_stockbajo, insert_venta, get_stock, get_sell_today, get_sell_today_d

conn=get_conexion()
cursor=conn.cursor()

def obtener_ventas_de_hoy():
    return get_sell_today()

def obtener_ventas_de_hoy_d():
    return get_sell_today_d()

def obtener_stockbajo():
    return get_stockbajo()

def obetener_stock(codigo):
    return get_stock(codigo)

def registrar_venta(datos_venta, info):
    try:
        insert_venta(cursor, datos_venta, info)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(e)