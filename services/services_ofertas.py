import sqlite3
from db.conexion import get_conexion
from repositories.repo_ofertas import active_ofertas, status_ofertas, disable_ofertas
from repositories.repo_inventario import get_item

def obtener_ofertas(oferta):
    info = get_item(oferta)
    if not info:
        return
    return info

def activar_oferta(oferta, valor):
    # Validaciones de regla de negocio
    if not oferta or valor <= 0:
        return False
    
    # Ejecución de persistencia
    return active_ofertas(oferta, valor)

def estado_oferta():
    return status_ofertas()

def quitar_oferta():
    return disable_ofertas()