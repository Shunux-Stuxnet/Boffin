from googlesearch import search

def find():
    quote = input("Who are you looking for? > ")
    print("[Searching your target on pastebin.]")
    for i1 in search("site:pastebin.com " + quote, stop=1000, pause=5):
        print(i1)
    print("[Searching your target on Google.]")
    for i2 in search(quote, stop=1000, pause=1):
        print(i2)




if __name__=="__main__":
   find()
