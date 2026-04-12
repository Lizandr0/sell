from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.console import Group
from rich.prompt import Prompt
import os

from services.services_inventario import obtener_inventario, registrar_producto, obtener_producto, eliminar_producto

def ui_eliminar(console):
    console.print(Panel('ELIMINAR PRODUCTO',subtitle='Buscar y eliminar por codigo'))

    codigo=Prompt.ask('CODIGO')
    if not codigo:
        console.print('Ingresa los datos wey')
        input('Presiona ENTER para continuar...')
        return
    consulta=obtener_producto(codigo)
    if not consulta:
        console.print(f'El codigo {codigo} no existe')
        input('Presiona ENTER para continuar...')
        return

    console.print(Panel(f'''
    INFORMACION DE {codigo}
    DESCIPCION: {consulta[2]}

    [bold bright_yellow]Desea eliminar? y/n                         
                  '''))
    o=Prompt.ask('->')
    if o.lower()=='n':
        console.print('No se hicieron cambios')
        input('Presiona ENTER para continuar...')
        return
    if o.lower()=='y':
        try:
            if eliminar_producto(codigo):
                os.system('clear')
                console.print(Panel(f"Se elimino el codigo {codigo}"))
                input('Presiona ENTER para continuar...')
                return
            else:
                os.system('clear')
                console.print('Error, no se elimino ningun registro')
                input('Presiona ENTER para continuar...')
                return
        except Exception as e:
            console.print(f"Error, {e}")
    else:
        console.print('Cancelado')

    

def ui_nuevo_producto(console):
    console.print(Panel('REGISTRAR PRODUCTO NUEVO'))
    
    while True:
        try:
            codigo=Prompt.ask('CODIGO')
            descripcion=Prompt.ask('DESCRIPCION')
            pc=float(Prompt.ask('PRECIO DE COMPRA'))
            pv=float(Prompt.ask('PRECIO DE VENTA'))
            stock=int(Prompt.ask('EXISTENCIAS'))
            break
        except ValueError:  
            os.system('clear')
            console.print(Panel('Ingresa valores validos', style='red'))

    if not codigo or not descripcion or not pc or not pv or not stock:
        os.system('clear')
        console.print('Campos vacios, intenta de nuevo')
        input('Presiona ENTER para continuar...')   
        return
    try:
        if registrar_producto(codigo, descripcion, pc, pv, stock):
            os.system('clear')
            console.print(Panel(f"{descripcion} [bold bright_green]Registrado con exito!", border_style='magenta'))
            input('Presiona ENTER para continuar...')
        else:
            os.system('clear')
            console.print('Error al registrar')
            input('Presiona ENTER para continuar...')
           
    except Exception as e:
        console.print('error',e)
        input('Presiona ENTER para continuar...')
    
def tabla_inicio_inventario():
    inventario = obtener_inventario()

    tabla_inventario=Table(border_style='#9999ff')
    tabla_inventario.add_column('CODIGO', style='cyan')
    tabla_inventario.add_column('DESCRIPCION', style='yellow')
    tabla_inventario.add_column('PRECIO C', style='green')
    tabla_inventario.add_column('PRECIO V', style='magenta')
    tabla_inventario.add_column('STOCK', style='blue')

    for item in inventario:
        tabla_inventario.add_row(f"{item[1]}", f"{item[2]}", f"Q {str(item[3])}", f"Q {str(item[4])}", f"{str(item[5])}")
    return Panel(tabla_inventario, border_style='#9999ff')


def inicio_inventario(console):
    while True:
        os.system('clear')
        console.print(Panel('INVENTARIO', border_style='#9999ff'), justify='center')
        panel_inventario=tabla_inicio_inventario()
        if not panel_inventario:
            console.print('No hay productos')


        console.print((panel_inventario), justify='center')

        console.print('\n1.Registrar |2.Actualizar |3.Eliminar |4. Salir',
                      justify='center')   

        s=Prompt.ask('ELIJE')

        if s=='4':
            console.print('ADIOS')
            break
        elif s=='1':
            ui_nuevo_producto(console)
        elif s=='2':
            console.print(Panel('[bold bright_yellow]NO DISPONIBLE', border_style='magenta'))
            input('Presiona ENTER para continuar...')
        elif s=='3':
            ui_eliminar(console)

        else:
            console.print('Opcion desconodida')