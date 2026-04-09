from repositories.repo_inventario import get_inventario, new_item, delete_item, get_item
from db.conexion import get_conexion
con=get_conexion()
cur=con.cursor()

def obtener_inventario():
    info=get_inventario()

    if not info:
        return 
    return info

def registrar_producto(codigo, descripcion, pc, pv, stock):
    try:
        new_item(cur,codigo, descripcion, pc, pv, stock)
        con.commit()
        return True
    except Exception as e:
        con.rollback()
        raise  e

def obtener_producto(codigo):
    info=get_item(codigo)
    if not info:
        return
    return info

def eliminar_producto(codigo):
    try:
        delete_item(cur, codigo)
        con.commit()
        return True
    except Exception as e:
        con.rollback()
        raise e