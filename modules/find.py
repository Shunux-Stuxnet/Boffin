from googlesearch import search

yellow = '\033[2;33m'
def find():
    kword = input("Who are you looking for? > ")
    print("[Searching your target on Doxbin.]")
    for i in search("site:doxbin.org " + kword, stop=1000, pause=1):
        print(i)
    print("[Searching your target on Pastebin.]")
    for i1 in search("site:pastebin.com " + kword, stop=1000, pause=5):
        print(i1)
    choice = input(yellow+"""
If you can't see anything in result that means there is nothing related to your keyword on either pastebin or doxbin. 
        Do you want to search your target on google? Type y/Y to search and n/N to finish.""")
    if(choice=="y" or choice == "Y"):
        print("[Searching your target on Google.]")
        for i2 in search(kword, stop=1000, pause=1):
            print(i2)
    else:
        print("\033[5;33;47m"+"Bye-Bye")


if __name__=="__main__":
   find()
