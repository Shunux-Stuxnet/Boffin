import time
import sys
from rich.console import Console
from rich.table import Table

from modules.find import find
from modules.eval import eval
from modules.dnsinfo import dnsinfo
from modules.subenum import subenum
from modules.linkscrap import linkscrap
from modules.metadata import meta
from modules.webinfo import webinfo

green="\u001b[32m"
Magenta="\033[95m"
yellow="\033[33m"
red="\033[31m"
cyan = '\033[36m' 

print(Magenta+"""
*═════════════════════════════════════════════════════════════════════*
                    ██████╗░░█████╗░███████╗███████╗██╗███╗░░██╗
                    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║████╗░██║
                    ██████╦╝██║░░██║█████╗░░█████╗░░██║██╔██╗██║
                    ██╔══██╗██║░░██║██╔══╝░░██╔══╝░░██║██║╚████║
                    ██████╦╝╚█████╔╝██║░░░░░██║░░░░░██║██║░╚███║
                    ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝
*═════════════════════════════════════════════════════════════════════*
""")
print(cyan+"""

                        =̵̺̟̞͌̓̔≠͚̘̫̓͑=̴̟̼̺̿͠͠=̵̺̟̞͌̓̔≠̞̠͎̽̕=̵͓̝͛̈́̒=̵̙̠̦͒̔͘≠̟͍̾̔͜͠≠͖͉̫͒͝≠̞̝͕́̽͝≠͚͍͐͛͌=̴̦̺̙̐͋͐=̵̝̪̞͐̕̚=̴̘̦̫̀̽=̵̢̙͉͑̚͝=̴̺͓͌̐̿͜≠̡̺̫̓̐̾=̵̪͕̼͋͝≠̘̟͋͆͜=̴̡̠͓̒̈́͠≠̟̺͎̈́̕͝≠̢̫̙̾͑=̵̟͙̻̐͊͘=̴͍̺͚͌͒=̴̢̝͍̈́̓͑=̵͎̻͚̽̒͆=̴̘̠͍͊̒̐=̴̼͇͊͐̓=̴̼͍͇̓̓̚=̵̘̞́̒͜͝=̴͕͇͖̔̓͘=̵͔̠̠̓̐͛≠̡̝̟͊̈́̒=̴̻̦͚͋́͐≠͖͚͙̐͆́=̵̢̼͍̒͐=̴̡̡̦͆̒͘=̴̡̡̦͆̒͘=̴̡̡̦͆̒͘=̴̡̦͆̒͘
                        =̵̢̟͍̔̈́       ╔══════════════════════╗       =̵̺̟̞͌̓̔
                        =̵͇̞͊͆͝        By : Team Shunux Space        =̴̝̟̐̾͜͝
                        ≠̠͔̐̐͒       ╚══════════════════════╝       =̴͙̻͔̒͋̓ 
                        =̴͎͇͔͑̕ https://github.com/Shunux-Stuxnet    =̵͔͙̠͊̾̀
                        =̵͚̫͓͆͛ https://github.com/N1xnonymous       =̴̫͆̈́͜͝ 
                        =̵͍̪̠̀͠͠ https://github.com/hanma-kun         =̴̞̝̠͐́
                        ≠͔͚̒̓͌                                      =̴̟͇͕̔́̔
                        =̵͖̠̿̀̚͜≠̝̝̓͒͝≠͖̫̼͌̈́̚=̴̫̠̙͌̓̒≠͖̻͑̾̔͜=̵̠͇͕͑̿̚=̵̠͕͚̔̀̕=̵̺͉͖̈́̒͌=̵̡̞͆͋̈́=̴͍̼͍̓̽=̵̦̻͙́͘͘=̴̡͎̠͐̈́͘≠͕̙͖̓͐̽=̴͉͔͆̓́͜=̴̦̙̈́̾̒=̴̢͎͍̒͒̐=̵͍̙͚̔̾͘=̴̠̞̈́͑͝≠͎̝͓͛͐̚=̵͕͓̠͋͒̈́=̵̙̞͉̿̈́̕=̵̟̼̼̓͝=̴̡͕̞͌͑≠͇̙̼̀͆̀=̵̢͕͔̓̓̕≠̢͙̞͆͐̕=̵̢͕̻̔̿̕≠͕̘͉͌̒̓≠̡͓̪͐̔͘≠̦̠͍̀͝=̴̺̦͕́̕͝≠͕̝̫͊̈́͝≠͕͍͎͌͋=̵̡̢̺̔̔͆=̴͖͖̝͋͆̽=̴̢̦̞͌̈́̓=̴̢̦̞͌̈́̓=̴̢̦̞͌̈́̓=̴̢̦̞͌̈́̓=̴̢̦̞͌̈́̓
    
    """)


print(yellow+"                              Input help to see all the options")

def help():
    table = Table(title="Tools list")
    table.add_column("Tool", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")
    table.add_column("Box Office", justify="right", style="green")
    table.add_row("1","Find", "Search keyword on Doxbin and pastebin, it also gives you option to search your keyword on Google.")
    table.add_row("2","Eval", "Check email validation, Check if it disposable email(eg. Temp Mail) and MX record.")
    table.add_row("3","Webinfo", "Check any website info.")
    table.add_row("4","DNSinfo", "Get the DNS records of any domain.")
    table.add_row("5","Subenum", "It gives all possible subdomains with first/last time seen data. Also adds if any TLSD is left from list")
    table.add_row("6","Link Scrapper", "Scrap all links present on any web page")
    table.add_row("7","MetaData extractor", "Extract the metadata of image or PDF.")
    table.add_row("exit","Exit", "Get out of this tool.")
    console = Console()
    console.print(table)



def boffin():
    inp=(input("Option>> "))
    if(inp=='1'):
        find()
    elif (inp=='2'):
        eval()
    elif (inp=='3'):
        webinfo()
    elif (inp=='4'):
        dnsinfo()
    elif (inp=='5'):
        subenum()
    elif (inp =='6'):
        linkscrap()
    elif (inp =='7'):
        meta()

    elif(inp=='exit'):
        exit()
    elif(inp=='help'):
        help()
    else:
        print(red+"Enter a valid option")
    while True:
        boffin()    
        
if __name__=="__main__":
   boffin()
