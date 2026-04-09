from rich.console import Console
from ui.ui_login import login_menu
from ui.ui_login import iniciar_sesion_ui
from ui.ui_menu_inicio import inicio
console=Console()

def main():
    login_menu(console)

if __name__ == "__main__":
    main()