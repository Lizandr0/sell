from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Group
from rich.columns import Columns
from ui.ui_colores import BANNER, BORDE, TEXTO, TEXTO2, ERROR, EXITO, PRECAUCION
from services.services_ventas import obtener_stockbajo, obtener_ventas_de_hoy
from services.services_meta_mensual import obtener_meta_mensual
from ui.ui_inventario import inicio_inventario
from ui.ui_ventas import main_ventas
from ui.ui_datos import main_datos
import os

def meta_resumen():
    meta=obtener_meta_mensual()
    if meta:
        meta_nombre=meta[0][0]
        meta_valor=meta[0][1]
        meta_actual=meta[0][2]

    return meta_nombre, meta_valor, meta_actual

def mostrar_stock_bajo(console):
    stock_bajo=obtener_stockbajo()
    if stock_bajo:
        console.print(f'Productos con stock bajo!', style=PRECAUCION)
        for item in stock_bajo:
            console.print(f"[{PRECAUCION}]Producto:[/] {item[2]}| [{PRECAUCION}]Stock:[/] {item[3]}")
    else:
        pass

def mostrar_ventas_del_dia(console):
    ventas=obtener_ventas_de_hoy()[0]
    table=Table(title='Ventas', border_style=BORDE)
    table.add_column('ID', style='bold #00ff00')
    table.add_column('Total', style=ERROR)
    table.add_column('Hora', style=PRECAUCION)

    for venta in ventas:
        table.add_row(f"{str(venta[0])}", f'Q {str(venta[1])}', f'{str(venta[3])}')
    
    return table


def inicio(console, user):
    while True:
        mostrar_ventas_del_dia(console)
        os.system('clear')
        txt=(Panel('''[bold #00ff00]

        1.VENDER
        2.INVENTARIO
        3.DATOS
        4.SALIR
                                ''', 
                                title='[bold bright_white]Menu', 
                                subtitle='[bold bright_white]Opciones', 
                                style=BORDE))

        total=(f"[bold {TEXTO}]TOTAL:[/bold {TEXTO}][white on red]Q {str(obtener_ventas_de_hoy()[1])}[/white on red]")
        console.print('i sell- by @Liz', style=f'bold black on {BORDE}', justify='center')   
        mostrar_stock_bajo(console)
        

        panel1=Panel(total,
                    border_style=BORDE)
        
        meta_nombre, meta_valor, meta_actual = meta_resumen()

        if meta_actual >= meta_valor:
            meta_status = f'''[bold {EXITO}]Meta alcanzada![/bold {EXITO}]
Tenemos ganancias:
[white on green]{meta_actual-meta_valor}'''
        else:
            meta_status = f'''[bold {PRECAUCION}]Meta no alcanzada[/bold {PRECAUCION}]
Nos faltan: [white on red]Q {meta_valor-meta_actual}'''


        panel_nombre_meta=Panel(f'[bold bright_white]{meta_nombre}[/bold bright_white]',
                                border_style=BORDE, 
                                title='[bold bright_white]Nombre', 
                                style=BORDE)
        
        panel_meta_valor=Panel(f'[white on green]Q {str(meta_valor)}[/white on green]', 
                               border_style=BORDE,
                               title='[bold bright_white]Valor', 
                               style=BORDE)
        
        panel_meta_actual=Panel(f'[white on green]Q {str(meta_actual)}[/white on green]', 
                                border_style=BORDE,
                                title='[bold bright_white]Avance', 
                                style=BORDE)
        
        panel_meta_status=Panel(meta_status, border_style=BORDE, title='[bold bright_white]Estado', style=BORDE)

        grupo_left=Panel(Group(mostrar_ventas_del_dia(console), panel1), title='[bold bright_white]Resumen del dia', style=BORDE)

        grupo_right=Panel(Group(panel_nombre_meta, panel_meta_valor, panel_meta_actual, panel_meta_status), title='[bold bright_white]Meta Mensual', style=BORDE)

        
        console.print(Panel(Columns([grupo_left, grupo_right]), title='[bold bright_white]Dashboard', border_style=BORDE), justify='center')
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