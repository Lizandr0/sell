from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.box import SIMPLE_HEAD
import os
from services.services_ventas_carrito import Carrito
from services.services_inventario import obtener_producto
from services.services_ventas import registrar_venta, get_stock, obtener_ventas_de_hoy

def ventas_hoy():
    info=obtener_ventas_de_hoy()[0]
    ventas=Table()
    ventas.add_column('ID', style='cyan')
    ventas.add_column('TOTAL', style='green')
    ventas.add_column('CLIENTE', style='yellow')
    ventas.add_column('VENDEDOR', style='magenta')
    ventas.add_column('HORA', style='blue')
    for id, total, vendedor, hora in info:
        ventas.add_row(f"{str(id)}", f"{str(total)}", "NONE", f"{vendedor}", f"{hora}")
    return ventas

def validar_stock(console, codigo, cantidad, carrito):
    consulta=get_stock(codigo)
    if not consulta:
        return False
    stock_bd=int(consulta[0])
    cantidad_carrito=0

    if codigo in carrito.items:
        cantidad_carrito=carrito.items[codigo]['cantidad']
    stock_disponible=stock_bd-cantidad_carrito

    if cantidad > stock_disponible:
        console.print("APP", "Stock insuficiente, existencias: "+str(stock_disponible))
        console.print(f'stock en bd: {stock_bd} | El carrito tiene: {cantidad_carrito} | stock disponible {stock_disponible}')
        return pedir_datos(console, carrito)

    elif stock_disponible<=0:
        console.print('APP', "Stock insuficiente, existencias: "+(str(stock_disponible)))
        console.print(f'stock en bd: {stock_bd} | El carrito tiene: {cantidad_carrito} | stock disponible {stock_disponible}')
        return pedir_datos(console, carrito)
    
    elif stock_disponible<=5:
        console.print('APP', 'Stock bajo, existencias: '+str(stock_disponible))
        console.print(f'stock en bd: {stock_bd} | El carrito tiene: {cantidad_carrito} | stock disponible {stock_disponible}')

    return True

def pedir_datos(console, carrito):
    console.print(Panel('Buscar por codigo'))
    codigo=Prompt.ask('[bold bright_yellow]CODIGO')

    if not codigo:
        console.print(Panel('Campo vacio'))
        input('Presiona ENTER para continuar...')
        return 
    
    info=obtener_producto(codigo)
    if not info:
        console.print(Panel('[bold red]El producto no existe'))
        input('Presiona ENTER para continuar...')
        return 
    
    console.print(Panel(f'''
    [bold yellow]DESCRIPCION: [bold green]{info[2]}
    [bold yellow]PRECIO SUGERIDO***: [bold green]{info[4]}
                        '''))
    while True:
        try:
            precio=float(Prompt.ask("[bold yellow]Precio autorizado"))
            cantidad=int(Prompt.ask('[bold yellow]Cantidad'))
            break
        except ValueError:
            console.print('[bold red]Ingresa un valor valido')

    if not cantidad:
        console.print('[bold red]Campos vacios')
        return
    
    if validar_stock(console, codigo, cantidad, carrito):
        carrito.agregar(codigo, info[2], cantidad, precio)
    else:
        console.print(Panel('Error, revisa el stock'))
        return  

def vender(console, carrito, vendedor):
    datos_venta=(carrito.obtener_total(), vendedor)

    info=carrito.items.items()
    if not info:
        console.print('[bold red]Carrito vacio')
    else:
        if registrar_venta(datos_venta, info):
            console.print(Panel('[bold bright_green]Registrado con exito'))
            input('Presiona ENTER para continuar...')
            carrito.vaciar()
        else:
            console.print('[bold bright_yellow]Error, al hacer el registro')
            return

def mostrar_carrito_ui(carrito, console):
    tabla = Table(title='[bold black on #9999ff]Productos en el carrito' ,border_style='magenta', box=SIMPLE_HEAD)
    tabla.add_column("Cód", style="cyan")
    tabla.add_column("Producto", style='magenta')
    tabla.add_column("Cant.", justify="right")
    tabla.add_column("Precio Q", justify="right")
    tabla.add_column("Subtotal Q", justify="right", style="green")

    for cod, info in carrito.items.items():
        tabla.add_row(
            cod, 
            info["nombre"], 
            str(info["cantidad"]), 
            f"Q {str(info['precio'])}", 
            f"Q {str(info['subtotal'])}"
        )
    console.print(tabla, justify='center')
    
    console.print(f"[bold]TOTAL A PAGAR: Q{carrito.obtener_total():.2f}[/bold]", justify='center')

def main_ventas(console, vendedor):
    mi_carrito=Carrito()
    while True:
        os.system('clear')

        ventas=ventas_hoy()
       
        console.print(Panel(ventas, title='Ventas del dia', 
                            border_style='#9999FF'), justify='center')
        
        console.print(f'\n1.Agregar al carrito| 2.Confirmar venta| 0.Vaciar y volver \n',
                      justify='center')
        
        if not mi_carrito.items:
            console.print('[black on bright_yellow]El carrito esta vacio')
        else:
            mostrar_carrito_ui(mi_carrito, console)
        o=Prompt.ask("[bold italic bright_yellow]Elije")

        if o=="0":
            mi_carrito.vaciar()
            break

        elif o=="1":
            pedir_datos(console, mi_carrito)

        elif o=="2":
            vender(console, mi_carrito, vendedor)

        else:
            console.print('Intenta de nuevo')