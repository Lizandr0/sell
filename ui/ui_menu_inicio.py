from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Group
from rich.columns import Columns
from ui.ui_colores import BANNER, BORDE, TEXTO, TEXTO2, ERROR, EXITO, PRECAUCION
from services.services_ventas import obtener_stockbajo, obtener_ventas_de_hoy
from ui.ui_inventario import inicio_inventario
from ui.ui_ventas import main_ventas
from ui.ui_datos import main_datos
import os

def mostrar_stock_bajo(console):
    stock_bajo=obtener_stockbajo()

    for item in stock_bajo:
        console.print(f"[{PRECAUCION}]Producto:[/] {item[2]}| [{PRECAUCION}]Stock:[/] {item[3]}")

def inicio(console, user):
    while True:
        os.system('clear')
        txt=(Panel('''[bold #00ff00]
        1.VENDER
        2.INVENTARIO
        3.DATOS
        4.SALIR
                                ''', 
                                title='Menu', 
                                subtitle='Opciones', 
                                style=BORDE))

        resumen=(f"""
-[bold #00ff00]Bienvenido {user}[/bold #00ff00]-

[bold {TEXTO}]Ventas:[/bold {TEXTO}][white on #9999ff]Q {str(obtener_ventas_de_hoy()[1])}[/white on #9999ff]
                 """)
        mostrar_stock_bajo(console)

        console.print(Panel(resumen, 
                            title='Resumen del dia', 
                            border_style=BORDE))
        console.print(txt)

        select=Prompt.ask('Elije')
        if select =='1':
            main_ventas(console, user)
        elif select =='2':
            inicio_inventario(console)
        elif select =='3':
            main_datos(console)
        elif select =='4':
            print("salir")
            break
        else:
            print(f'Error, opcion {select} desconocida')