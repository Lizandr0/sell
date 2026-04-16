from rich.panel import Panel
from rich.prompt import Prompt

from services.services_inventario import obtener_producto, actualizar_producto

def pedir_datos(console):
    new_pc=Prompt.ask('Precio de compra')
    new_pv=Prompt.ask('Precio de venta')
    new_stock=Prompt.ask('Stock')

    new_data=(new_pc, new_pv, new_stock)

    if not all(new_data):
        console.print('Campos vacios bro, intenta de nuevo')
        input('Presiona ENTER para continuar...')
        return
    return new_pc, new_pv, new_stock

def actualizar(console, codigo):
    console.print(Panel('[bold yellow]Solo puedes cambiar precio de compra, precio de venta y stock', style='#9999ff'))
    pc, pv, stock=pedir_datos(console)
    if actualizar_producto(pc, pv, stock, codigo):
        console.print('Actualizado con exito!')
        input('Prsiona enter para continuar...')
        return
    else:
        console.print('error al registrar los cambios')
        input('Presiona enter para continuar...')
        return



def main_actualizar_datos(console):
    codigo=Prompt.ask('Codigo')
    if not codigo:
        console.print('Ingresa el codigo bro')
        return
    item=obtener_producto(codigo)
    if not item:
        console.print(f'[bold yellow]No hay producto registrado con el codigo: [black on red]{codigo}')
        input('Presiona ENTER para regresar...')
        return
    
    console.print(Panel(f'''
[bold bright_yellow]Informacion de {codigo}:[bold bright_yellow]
[bold bright_white]
    Producto: {item[2]}
    Precio de compra: {str(item[3])}
    Precio de venta: {str(item[4])}  
    Existencias: {str(item[5])}
                        '''))
    s=Prompt.ask('Editar? y=si \ n=no')
    if s.lower()=='y':
        actualizar(console, codigo)
    elif s.lower()=='n':
        console.print('Cancelado')
        input('Presiona ENTER para continuar...')
        return
    else:
        return