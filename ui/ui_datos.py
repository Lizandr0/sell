from rich.panel import Panel
from rich.prompt import Prompt
import os
from ui.ui_colores import BORDE, TEXTO, TEXTO2, ERROR
from ui.ui_meta_mensual import main_meta

def main_datos(console):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        txt=('''[bold bright_white]
        1. Meta Mensual
        2. Reporte de Ventas
        3. Reporte de Inventario
        0. Regresar
            
            ''')
        
        console.print(Panel('DATOS', style=TEXTO))
        opciones=(Panel(txt, style=TEXTO2))
        console.print(opciones)



        s=Prompt.ask('[bold black on yellow]Seleccione una opcion', choices=['1','2','3','0'])

        if s=='1':
            console.print(Panel('Meta Mensual'), style=BORDE)
            main_meta(console)
        elif s=='0':
            break
        else:
            console.print(Panel('Opcion no disponible'), style=ERROR)
            Prompt.ask('Presione enter para regresar')