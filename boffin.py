import time
import sys
from rich.console import Console
from rich.table import Table
from find import find
from eval import eval

green="\u001b[32m"
Magenta="\033[95m"
yellow="\033[33m"
red="\033[31m"
cyan = '\033[36m' 

print(Magenta+"""

                    ██████╗░░█████╗░███████╗███████╗██╗███╗░░██╗
                    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║████╗░██║
                    ██████╦╝██║░░██║█████╗░░█████╗░░██║██╔██╗██║
                    ██╔══██╗██║░░██║██╔══╝░░██╔══╝░░██║██║╚████║
                    ██████╦╝╚█████╔╝██║░░░░░██║░░░░░██║██║░╚███║
                    ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝
    
    """)

print(cyan+"                                                        By : Team Shunux Space")
print(yellow+"  Input help to see all the options")

def help():
    table = Table(title="Tools list")
    table.add_column("S.No", justify="right", style="cyan", no_wrap=True)
    table.add_column("Tool", style="magenta")
    table.add_column("Description", justify="right", style="green")
    table.add_row("1", Find", "Search anything if that is in Pastebin, it also searches the keyword on google.")
    table.add_row("2", Eval", "Check email validation and MX record.")
    console = Console()
    console.print(table)



def boffin():
    inp=(input("Option-> "))
    if(inp=='1'):
      find()
    elif(inp=='2'):
      eval()
    elif(inp=='exit'):
        exit()
    elif(inp=='help'):
        print(green+"""Tools available
        
          1. FindMe    Find anyone over interne using Pastbin and google. (Doxbin could be added and other services too, analyzing their relevnce if they make any to this tool)
            In making, will update soon
            usage : type exit to stop
            """)
    else:
        print(red+"Hello Moto, Have a look at options by inputting "help".)
    while True:
        boffin()    
        
if __name__=="__main__":
   boffin()
