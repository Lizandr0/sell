from db.conexion import get_conexion

def get_meta_mensual():
    con=get_conexion()
    cur=con.cursor()
    cur.execute("""
                            SELECT m.nombre,
                            m.meta,
                                IFNULL(SUM(v.total),0) AS valor_actual 
                                FROM META m
                                LEFT JOIN ventas v
                                ON v.fecha BETWEEN m.fecha_inicio AND m.fecha_fin
                                WHERE m.activa=1 
                                GROUP BY m.id

                                """)
    return cur.fetchall()

def insertar_meta_mensual(cursor, nombre, valor, fecha_inicio, fecha_fin):
    try:
        cursor.execute('UPDATE META SET activa=0')
        cursor.execute("""
                        INSERT INTO META (nombre, meta, fecha_inicio, fecha_fin) 
                        VALUES (?, ?, ?, ?)
                        """, (nombre, valor, fecha_inicio, fecha_fin))
    except Exception as e:
        Exception(f"Error al insertar meta mensual: {e}")