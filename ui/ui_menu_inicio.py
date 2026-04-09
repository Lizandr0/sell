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
        meta_resumen=(f"""
[bold #00ff00]Nombre:[/] 
{meta_nombre} 
[bold #00ff00]Valor:[/]
Q{meta_valor}  
[bold #00ff00]Avance:[/] 
Q{meta_actual}""")
    else:
        meta_resumen="[bold #00ff00]Meta Mensual:[/] No hay meta activa" 
        
    if meta_actual >= meta_valor:
        meta_resumen += f"""
    \n[bold #00ff00]¡Meta alcanzada![/bold #00ff00]
    Ganancias del mes: [black on green]
    Q {meta_actual - meta_valor}[/black on green]"""
            
    elif meta_actual >= meta_valor * 0.75:
        meta_resumen += f"""\n[bold #00ff00]¡Casi alcanzas la meta Nos faltan [balck on red]
        Q {meta_valor - meta_actual}[/black on red]![/bold #00ff00]"""
    else:
        meta_resumen += f"""\n[bold #00ff00]Nos faltan [black on red]
Q {meta_valor - meta_actual}[/black on red] 
para llegar a la meta.[/bold #00ff00]
"""
    return meta_resumen

def mostrar_stock_bajo(console):
    stock_bajo=obtener_stockbajo()

    for item in stock_bajo:
        console.print(f"[{PRECAUCION}]Producto:[/] {item[2]}| [{PRECAUCION}]Stock:[/] {item[3]}")

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
        
        mostrar_stock_bajo(console)

        panel1=Panel(total,
                    border_style=BORDE)
        
        panel_meta=Panel(meta_resumen(), title='[bold bright_white]Meta Mensual', border_style=BORDE)
        
        grupo_left=Panel(Group(mostrar_ventas_del_dia(console), panel1), title='[bold bright_white]Resumen del dia', style=BORDE)

        grupo_right=Group(panel_meta)

        
        console.print(Columns([grupo_left, grupo_right]))
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