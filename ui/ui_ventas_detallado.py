from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.prompt import Prompt
from services.services_ventas import obtener_ventas_de_hoy, obtener_ventas_de_hoy_d
def mostrar_ventas():
    info=obtener_ventas_de_hoy()[0]

    tabla=Table()
    tabla.add_column('ID')
    tabla.add_column('Cliente')
    tabla.add_column('Total')
    tabla.add_column('Hora')
    tabla.add_column('Vendedor')

    for i in info:
        tabla.add_row(f"{str(i[0])}", "0", f'Q {str(i[1])}', f'{str(i[3])}', f'{str(i[2])}')
    return tabla

def mostrar_ventas_detallado():
    info=obtener_ventas_de_hoy_d()
    tabla=Table()
    tabla.add_column('ID venta')
    tabla.add_column('ID producto')
    tabla.add_column('Descripcion')
    tabla.add_column('Cantidad')
    tabla.add_column('Precio u')
    tabla.add_column('Subtotal')
    if not info:
        tabla.add_row('none', 'none', 'none', 'none', 'none', 'none')
    else:
        for i in info:
            tabla.add_row(str(i[1]), i[2], i[3], str(i[4]), f'Q{i[5]}', f'Q{i[6]}')
        return tabla

def main_ventas_d(console):
    tabla_ventas=mostrar_ventas()
    tabla_ventas_d=mostrar_ventas_detallado()
    while True:
        console.print(Panel('Resumen de ventas del dia'))
        panelv=Panel(tabla_ventas, title='Ventas del dia')
        panelvd=Panel(tabla_ventas_d, title='Detalle de las ventas del dia')
        total_ventas=obtener_ventas_de_hoy()[1]

        console.print(panelv, justify='center')
        console.print(panelvd, justify='center')
        console.print(Panel(f"Total de las ventas del dia: Q{str(total_ventas)}"), justify='center')


        s=Prompt.ask('0.Volver')

        if s=='0':
            break
