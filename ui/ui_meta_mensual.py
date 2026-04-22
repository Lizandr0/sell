from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Group
from rich.columns import Columns
import os
from ui.ui_colores import BANNER, BORDE, TEXTO, TEXTO2, ERROR, EXITO, PRECAUCION
from services.services_meta_mensual import registrar_meta_mensual

def pedir_datos_meta(console):
    console.print(Panel('Ingrese los datos de la meta mensual', title='[bold bright_white]Meta Mensual', style=BORDE))
    nombre=Prompt.ask('Nombre de la meta')
    valor=Prompt.ask('Valor de la meta')
    fehcha_inicio=Prompt.ask('Fecha de inicio (YYYY-MM-DD)')
    fecha_fin=Prompt.ask('Fecha de fin (YYYY-MM-DD)')
    return nombre, valor, fehcha_inicio, fecha_fin

def validar_datos_meta(nombre, valor, fecha_inicio, fecha_fin):

    if not nombre or not valor or not fecha_inicio or not fecha_fin:
        return False, 'Todos los campos son obligatorios.'
    try:
        valor=float(valor)
        if valor <= 0:
            return False, 'El valor de la meta debe ser un número positivo.'
    except ValueError:
        return False, 'El valor de la meta debe ser un número.'
    # Validar formato de fechas
    try:
        from datetime import datetime
        datetime.strptime(fecha_inicio, '%Y-%m-%d')
        datetime.strptime(fecha_fin, '%Y-%m-%d')
    except ValueError:
        return False, 'Las fechas deben tener el formato YYYY-MM-DD.'
    return True, ''

def guardar_meta(console):
    nombre, valor, fecha_inicio, fecha_fin=pedir_datos_meta(console)
    valido, mensaje=validar_datos_meta(nombre, valor, fecha_inicio, fecha_fin)
    if not valido:
        console.print(Panel(mensaje, style=ERROR))
        input('Presione Enter para continuar...')
        return
    
    if registrar_meta_mensual(nombre, valor, fecha_inicio, fecha_fin):
        console.print(Panel('Meta mensual registrada exitosamente.', style=EXITO))
        input('Presione Enter para continuar...')
    else:
        console.print(Panel('Error al registrar la meta mensual.', style=ERROR))
        input('Presione Enter para continuar...')

def main_meta(console):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        txt=('''
1. Ingresar Meta Mensual
0. Regresar
             ''')
        console.print(Panel(txt, title='[bold bright_white]Meta Mensual', style=BORDE))
        s=Prompt.ask('Elige una opción', choices=['1', '0'])

        if s=='1':
            guardar_meta(console)
        elif s=='0':
            break
        else:
            console.print(Panel('Opción no válida. Intente de nuevo.', style=ERROR))
            input('Presione Enter para continuar...')