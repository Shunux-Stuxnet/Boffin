from googlesearch import search
target = input("Who are you looking for? > ")

print("[Searching your target on pastebin.]")
for x in search("site:pastebin.com " + target, stop=100, pause=5):
    print(x)
print("[Searching your target on Google.]")
for y in search(target, stop=100, pause=5):
    print(y)    
