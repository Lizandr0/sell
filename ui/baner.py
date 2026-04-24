from rich.panel import Panel
import sys
def banner(console):
    console.print(f'i-sell | Version: 1.0 | SO: {sys.platform}', style=f'bold #000000 on #9999ff', justify='center')  

    txt='''                          
                    ▄▄ ▄▄ 
                     ██ ██
 ▀▀                  ██ ██
 ██      ▄██▀█ ▄█▀█▄ ██ ██
 ██ ▀▀▀▀ ▀███▄ ██▄█▀ ██ ██
▄██     █▄▄██▀▄▀█▄▄▄▄██▄██
             -by Lizandr0-
                          
                          '''
    console.print(txt, style="black on #9999ff", justify='center')