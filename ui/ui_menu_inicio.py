from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.box import SIMPLE_HEAD, MINIMAL
from rich.console import Group
from rich.columns import Columns
from ui.ui_colores import BANNER, BORDE, TEXTO, TEXTO2, ERROR, EXITO, PRECAUCION
from services.services_ventas import obtener_stockbajo, obtener_ventas_de_hoy
from services.services_meta_mensual import obtener_meta_mensual
from ui.ui_inventario import inicio_inventario
from ui.ui_ventas import main_ventas
from ui.ui_datos import main_datos
import os
import sys

def meta_resumen():
    meta=obtener_meta_mensual()
    if meta:
        meta_nombre=meta[0][0]
        meta_valor=meta[0][1]
        meta_actual=meta[0][2]

    return meta_nombre, meta_valor, meta_actual

def mostrar_stock():
    stock_bajo=obtener_stockbajo()

    tabla=Table(title=f'[{PRECAUCION}]', border_style=BORDE, box=MINIMAL)
    tabla.add_column('[bold bright_white]Producto', style='cyan')
    tabla.add_column('[bold bright_white]Stock', style='bold black on magenta')
    if stock_bajo:
        for item in stock_bajo:
            tabla.add_row(f'{item[2]}', f'{item[5]}')
    else:
        tabla.add_column('exist', '0')
    return tabla

def mostrar_ventas_del_dia():
    ventas=obtener_ventas_de_hoy()[0]
    table=Table(border_style=BORDE, box=MINIMAL)
    table.add_column('[bold bright_white]ID', style='bold #00ff00')
    table.add_column('[bold bright_white]Total', style='bold white on #9999ff')
    table.add_column('[bold bright_white]Hora', style=PRECAUCION)

    for venta in ventas:
        table.add_row(f"{str(venta[0])}", f'Q {str(venta[1])}', f'{str(venta[3])}')
    
    return table


def inicio(console, user):
    while True:
        os.system('clear')

        console.print(f'i sell by @Lizandr0 | Version: 1.0 | SO: {sys.platform}', style=f'black on {BORDE}', justify='center')  
        
        meta_nombre, meta_valor, meta_actual = meta_resumen()

        if meta_actual >= meta_valor:
            meta_status = f'''[bold {EXITO}]Llegamos![/bold {EXITO}]'''
            total_status=f'[bold bright_white]Si, ganancias: [bold {EXITO}]Q {meta_actual-meta_valor}'
        else:
            meta_status = f'''[bold {ERROR}]Falta :([/bold {ERROR}]'''
            total_status=f'[bold bright_white]No, faltan: [{ERROR}]Q {meta_valor-meta_actual}'
        
        #tabla meta-------------------------------------------------------------------------------
        tabla=Table(title=f"[bold {BORDE}]{meta_nombre}", style=BORDE, box=MINIMAL)
        tabla.add_column('[bold bright_white]Meta', style='bold black on #9999ff')
        tabla.add_column("[bold bright_white]Avance", style=f'bold {EXITO}')
        tabla.add_column('[bold bright_white]Estado')
        tabla.add_row(f'Q {str(meta_valor)}', f'Q {str(meta_actual)}', meta_status)
        
        panel_meta_status=Panel(total_status, border_style=BORDE, 
                                title='[bold bright_white]Rentable?', 
                                style=BORDE)
        #---------------------------------------meta---------------------------------------------

        #stock--------------------------------------------
        panel_stock=Panel(mostrar_stock(), style=BORDE, title=f'[{PRECAUCION}]Stock bajo!', width=39)

        #Grupo ventas del dia------------------------------
        usuario_activo=Panel(f"[{EXITO}]@{user}",title="[bold bright_white]Usuario Activo", style=BORDE)

        total=(f"[bold bright_white]TOTAL: [/bold bright_white][{ERROR}]Q {str(obtener_ventas_de_hoy()[1])}[/]")
        
        panel_total_ventas_del_dia=Panel(total,
                    border_style=BORDE)
        
        grupo_ventas=Panel(Group(mostrar_ventas_del_dia(), panel_total_ventas_del_dia), 
                           title=f'[bold bright_white]Ventas del dia',
                           style=BORDE)
        grupo_left=Group(usuario_activo, grupo_ventas)
        
        #Grupos izquirda y derecha-----------------------
        grupo_meta=Panel(Group(tabla, panel_meta_status), 
                          title='[bold bright_white]Meta Mensual', 
                          style=BORDE)
        
        grupo_right=Group(grupo_meta, panel_stock)

        
        console.print(Panel(Columns([grupo_left, grupo_right]), 
                            title='[bold bright_white]Dashboard', 
                            border_style=BORDE), justify='center')
        
        console.print(f'\n1.VENDER|2.INVENTARIO|3.DATOS|0.SALIR|  -{sys.platform}-',
                      justify='center')   

        select=Prompt.ask('Elije')
        if select =='1':
            main_ventas(console, user)
        elif select =='2':
            inicio_inventario(console)
        elif select =='3':
            main_datos(console)
        elif select =='0':
            print("salir")
            break
        else:
            print(f'Error, opcion {select} desconocida')