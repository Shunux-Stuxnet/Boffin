import requests
import json
import socket
import time
from pprint import pprint
wapapi = 'wgYvzU4pKd7i4UMcSPYTaKCjk2I1ILm7gKMbEHlj'
def webinfo():
    web = input("Enter the website you want to know about? > ")

    ip = socket.gethostbyname(web)
    resp = requests.get(f'https://ipapi.co/{ip}/json/').json()

    url = "https://domain-reputation.whoisxmlapi.com/api/v2?apiKey=at_jrNCEHl52VXlCpYol8eQt0me9Qub1&domainName="+web
    response = requests.request("GET", url)
    pjson = json.loads(response.text)
    

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
    print("Domain Reputation\n==================\n")
    print (json.dumps(pjson, indent=3))
    time.sleep(2)
    print("\nDomain Technologies\n===================\n")
    print (json.dumps(pretty_json, indent=2))
    time.sleep(3)
    print("\nAdditional data\n===============")
    pprint(resp)

if __name__=="__main__":
   webinfo()
