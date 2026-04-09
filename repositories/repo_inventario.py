from db.conexion import get_conexion
import sqlite3

con=get_conexion()
cursor=con.cursor()


def get_inventario():
    cursor.execute('SELECT* FROM inventario')
    return cursor.fetchall()

def get_item(codigo):
    cursor.execute('SELECT* FROM inventario WHERE codigo=?',(codigo,))
    producto=cursor.fetchone()
    return producto

def new_item(cur, codigo, descripcion, pc, pv, stock):
    cur.execute('''
INSERT INTO inventario(codigo, descripcion, precio_c, precio_v, stock)
VALUES(?,?,?,?,?)
                    ''', (codigo, descripcion, pc, pv, stock))

def delete_item(cur, codigo):
    cur.execute('DELETE FROM inventario WHERE codigo=?',(codigo,))
def update_item(cur, datos):
    cur.exeute('''
            UPDATE inventario SET()
               ''')