from rich.prompt import Prompt
from rich.panel import Panel
from services.services_login import iniciar_sesion
from services.services_login import crear_usuario
from ui.baner import banner
from ui.ui_menu_inicio import inicio
from ui.ui_colores import BANNER, BORDE, TEXTO, TEXTO2, ERROR, EXITO, PRECAUCION
import os

def get_usuario_activo():
    return usuario

def iniciar_sesion_ui(console):
    console.print(Panel('INICIAR SESION', border_style=BORDE, style='#08FF08'))
    global usuario
    usuario=Prompt.ask('USUARIO')
    contrasena=Prompt.ask('CONTRASENA', password=True)

    if not usuario or not contrasena:
        console.print('Campos vacios', style=TEXTO2)
        input('->')
        return iniciar_sesion_ui(console)
    try:    
        if iniciar_sesion(usuario, contrasena):
            console.print(f'\nBienvenido {usuario}!', style=EXITO)
            input('->')
            os.system('clear')
            inicio(console, usuario)
        else:
            console.print('Usuario o contrase;a incorrectos rey', style=ERROR)
            input('->')
    except Exception as e:
        print(e)

def crear_usuario_ui(console):
    console.print(Panel('CREAR USUARIO', border_style=BORDE, style='#08FF08'))

    new_user=Prompt.ask(f'[bold {BANNER}]Crea un nombre de usuario')
    new_pass=Prompt.ask(f'[bold {BANNER}]Crea una contrasena', password=True)
    conf_pass=Prompt.ask(f'[bold {BANNER}]confirma tu contrasena', password=True)

    if not new_user or not new_pass or not conf_pass:
        console.print("campos vacios bro, intenta de nuevo", style=PRECAUCION)
        return login_menu(console)
    if new_pass != conf_pass:
        console.print('Las contrsenas no coinciden pa! hazlo de nuevo', style=ERROR)
        return login_menu(console)
    try:
        crear_usuario(new_user, conf_pass)
        console.print('Ya tienes usario pa! puedes iniciar sesion', style=EXITO) 
        input('->')
        login_menu(console)
    except Exception as e:
        console.print('Error',e, style=ERROR)

    

def login_menu(console):
    while True:
        banner(console)
        console.print(Panel('''[bold #ba8cbe]

    1.INICIAR SESION
    2.CREAR USUARIO
    3.SALIR                  
                    ''', title='-Sistema de ventas e inventario-', border_style="#c7a3d2"))
        x=Prompt.ask('Elije')
        if not x:
            os.system('clear')
            console.print('Tienes que ingresar los datos no seas mamon', style=PRECAUCION)
            return login_menu(console)

        if x=='1':
            iniciar_sesion_ui(console)
        elif x=='2':
            crear_usuario_ui(console)
        elif x=='3':
            console.print('Adios rey')
            break
        else:
            os.system('clear')
            console.print('No mas no das ni una padre santo, solo hay 3 opciones rey', style=ERROR)