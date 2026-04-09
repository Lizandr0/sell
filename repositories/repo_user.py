from db.conexion import get_conexion
con = get_conexion()
cur=con.cursor()

def get_user(user, password):
    cur.execute('SELECT* FROM users WHERE nickname=? AND password=?',(user,password,))
    return cur.fetchall()

def new_user(cursor,user, password):
    try:
        cursor.execute('INSERT INTO users(nickname, password) VALUES(?,?)', (user, password))
    except Exception as e:
        raise Exception('Error en la base de datos')