from googlesearch import search
from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

def find():
    quote = input("Who are you looking for? > ")
    print("[Ищем на doxb]")
    for i1 in search("site:doxbin.org " + quote, stop=1000, pause=1):
        #print(i1)
        table.add_row("Doxbin", print(i1), "jy")
        print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Doxbin', 'Results'], tablefmt='orgtbl'))
    print("[Searching your target on pastebin.]")
    for i2 in search("site:pastebin.com " + quote, stop=1000, pause=5):
        print(i2)
    print("[Searching your target on Google.]")
    for i3 in search(quote, stop=1000, pause=1):
        print(i3)




if __name__=="__main__":
   find()