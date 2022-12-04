import requests
from bs4 import BeautifulSoup

def linkscrap():
    print("This feature will give all the links of the web as output")
    url=input("Enter the domain (with protocol https or http > ")
    print('')
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    for link in soup.find_all('a'):
        res=link.get('href')
        print(res)
        
if __name__=="__main__":
    linkscrap()