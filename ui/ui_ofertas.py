from rich.prompt import Prompt
from rich.panel import Panel
import os

from services.services_ofertas import activar_oferta, obtener_ofertas, estado_oferta, quitar_oferta
from ui.ui_colores import EXITO, ERROR

def activar_ofertas(console):
    console.print(Panel('Activar ofertas'), justify='center')
    oferta=Prompt.ask('Ingrese el codigo de la oferta')
    
    info=obtener_ofertas(oferta)
    if not info:
        console.print(Panel('No se encontró el producto con el código proporcionado'), style='bold red')
        input('Presione Enter para continuar...')
        return
    console.print(Panel(f'Producto: {info[2]} | Precio actual: Q{info[4]}'))

    while True:
        try:
            valor=int(Prompt.ask('Ingrese el nuevo precio'))
            break
        except ValueError:
            console.print(Panel('Por favor, ingrese un número válido'), style='bold red')
            input('Presione Enter para intentar nuevamente...')

    if activar_oferta(oferta, valor):
        console.print(Panel('Oferta activada exitosamente'), style='bold green')
        input('Presione Enter para continuar...')
    else:
        console.print(Panel('Error al activar la oferta'), style='bold red')
        input('Presione Enter para continuar...')


def main_ofertas(console):
    while True:
        os.system('clear')

        estado=estado_oferta()

        if estado == 0 or estado == None:
            console.print(Panel(f'[bold {ERROR}]No hay ofertas activas[/bold {ERROR}] existencias: {estado}'), justify='center')
        else:
            console.print(Panel(f'[bold {EXITO}]OFERTA ACTIVA![/bold {EXITO}] existencias: {estado}'), justify='center')

        console.print('1.Activar Ofertas | 2.Quitar Ofertas | 0.Salir', justify='center')

        s=Prompt.ask('Elije')

        if s=='1':
            activar_ofertas(console)
        elif s=='2':
            if quitar_oferta():
                console.print(Panel('Oferta desactivada exitosamente'), style='bold green')
                input('Presione Enter para continuar...')
            else:
                console.print(Panel('Error al desactivar la oferta'), style='bold red')
                input('Presione Enter para continuar...')
        elif  s=='0':
            return