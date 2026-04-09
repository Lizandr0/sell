from repositories.repo_user import get_user
from repositories.repo_user import new_user
from db.conexion import get_conexion

def iniciar_sesion(user, password):
    user_db=get_user(user, password)
    if not user_db:
        return False
    return user_db

def crear_usuario(user, password):
    con=get_conexion()
    cur=con.cursor()
    try:
        new_user(cur, user, password)
        con.commit()
    except Exception as e:
        raise Exception('error XXX')