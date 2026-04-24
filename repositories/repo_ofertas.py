from db.conexion import get_conexion

con=get_conexion()
cur=con.cursor()
def active_ofertas(oferta, valor):
    cur.execute("SELECT SUM(stock) FROM inventario")
    total_stock=cur.fetchone()[0] or 0
    
    try:
        cur.execute("UPDATE inventario SET stock=0 ")
        cur.execute("""UPDATE inventario 
                    SET precio_v=?,
                    stock=?
                    WHERE codigo=?""", (valor,total_stock, oferta))
        con.commit()
        return True
    except Exception as e:
        con.rollback()
        print(f"Error: {e}")
        return False

def status_ofertas():
    cur.execute("SELECT stock FROM inventario WHERE codigo=?", ('oferta',))
    return cur.fetchone()[0] or 0

def disable_ofertas():
    try:
        cur.execute("UPDATE inventario SET stock=0 WHERE codigo='oferta'")
        con.commit()
        return True
    except Exception as e:
        con.rollback()
        print(f"Error: {e}")
        return False