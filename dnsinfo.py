import requests

def dnsinfo():
    print("This feature will dig the DNS record.\n")
    domain = input("Enter the domain: >")
    url = "https://api.hackertarget.com/dnslookup/"
    req = {"q": domain}
    response = requests.request("GET", url, params=req)
    print(response.text)

if __name__=="__main__":
   dnsinfo()