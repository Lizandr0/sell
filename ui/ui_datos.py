from rich.panel import Panel
def main_datos(console):
    while True:
        txt=('''
    Estos datos no se pueden modificar!
            
        1.VER REGISTRO DE VENTAS
        2.USUARIOS
        3.INVENTARIO
            
            ''')
        console.print(Panel('DATOS'))

        opciones=(Panel(txt))

        console.print(Panel(opciones))
        