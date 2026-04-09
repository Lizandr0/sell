from db.conexion import get_conexion

con=get_conexion()
cur=con.cursor()

def get_sell_today():
    cur.execute("""SELECT id_venta, total, vendedor, strftime('%H:%M', fecha) as hora_venta 
                FROM ventas
                WHERE date(fecha)=date('now', 'localtime')""")
    ventas_de_hoy=cur.fetchall()
    
    cur.execute("SELECT SUM(total) FROM ventas WHERE date(fecha)=date('now', 'localtime')")
    total_ventas_de_hoy=cur.fetchone()[0]
    
    return ventas_de_hoy, total_ventas_de_hoy

def get_stockbajo():
    cur.execute('SELECT* FROM inventario WHERE stock<=5')
    return cur.fetchall()

def get_stock(codigo):
    cur.execute('SELECT COALESCE(stock,0) AS stock FROM inventario WHERE codigo=?', (codigo,))
    return cur.fetchone()

def insert_venta(cursor, datos_venta, info):
    try:
        cursor.execute('''
                INSERT INTO ventas (total, vendedor) VALUES(?,?)
                        ''',(datos_venta))
        venta_id=cursor.lastrowid

        for codigo, datos in info:
            cursor.execute('''
                        INSERT INTO ventas_detallado(
                                    id_venta, 
                                    id_producto, 
                                    descripcion, 
                                    cantidad,
                                    precio_unitario,
                                    subtotal ) VALUES(?,?,?,?,?,?)
            ''',(venta_id, codigo, datos['nombre'], datos['cantidad'], datos['precio'], datos['subtotal']))

            cursor.execute(f'UPDATE inventario SET stock=stock-{datos['cantidad']} WHERE codigo=?',(codigo,))
    except Exception as e:
        cursor.execute('ROLLBACK')
        raise e