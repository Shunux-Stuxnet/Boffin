import requests
import json
import socket
import time
from pprint import pprint
wapapi = 'wgYvzU4pKd7i4UMcSPYTaKCjk2I1ILm7gKMbEHlj'
web = input("Enter the website you want to know about? > ")
def webinfo():

    ip = socket.gethostbyname(web)
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()

    list_response = []
    webs="https://"+web
    url = 'https://api.wappalyzer.com/lookup/v2/?urls=' + webs + '&sets=meta,locale,security,trackers,events'
    headers = {'x-api-key' : wapapi}
    r = requests.get(url, headers=headers)
    list_response.append(r.json())
    pretty_json = json.loads(r.text)

    print("Domain IP\n==========\n")
    print(ip)
    time.sleep(1)
    print("\nDomain Technologies\n===================\n")
    print (json.dumps(pretty_json, indent=2))
    time.sleep(2)
    print("\nAdditional data\n===============")
    pprint(response)

if __name__=="__main__":
   webinfo()
