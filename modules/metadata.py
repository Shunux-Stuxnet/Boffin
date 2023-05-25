import requests
import json
import socket
import time
from pprint import pprint

DEFAULT_API_KEY_1 = 'at_vGmy0FhsoYe4Pf7knT9qmwrARCnP0'
DEFAULT_API_KEY_2 = 'h4SKv1Mx8ha36hVewwkPN5x2mptU7NQC6FvupB0U'

def get_user_api_key_1():
    print("\nGet your own API key at https://domain-reputation.whoisxmlapi.com/api/signup?lang=en\n")
    time.sleep(2)
    api_key = input("Enter your API key for getting additional domain information (Press enter key if you want to use dafault key but then there's high chance of failure.): ")
    if api_key:
        return api_key
    else:
        return DEFAULT_API_KEY_1

def get_user_api_key_2():
    print("\nGet your own API key at https://www.wappalyzer.com/apikey/\n")
    time.sleep(2)
    api_key = input("Enter your API key for getting domain technology information (Press enter key if you want to use dafault key but then there's high chance of failure.): ")
    if api_key:
        return api_key
    else:
        return DEFAULT_API_KEY_2

def webinfo():
    api_key_1 = get_user_api_key_1()
    api_key_2 = get_user_api_key_2()
    web = input("\nEnter the website you want to know about: ")

    ip = socket.gethostbyname(web)
    resp = requests.get(f'https://ipapi.co/{ip}/json/').json()

    url = f"https://domain-reputation.whoisxmlapi.com/api/v2?apiKey={api_key_1}&domainName={web}"
    response = requests.get(url)
    pjson = json.loads(response.text)

    list_response = []
    webs = "https://" + web
    url = f'https://api.wappalyzer.com/lookup/v2/?urls={webs}&sets=meta,locale,security,trackers,events'
    headers = {'x-api-key': api_key_2}
    r = requests.get(url, headers=headers)
    list_response.append(r.json())
    pretty_json = json.loads(r.text)

    print("Domain IP\n==========\n")
    print(ip)
    time.sleep(1)
    print("Domain Reputation\n==================\n")
    print(json.dumps(pjson, indent=3))
    time.sleep(2)
    print("\nDomain Technologies\n===================\n")
    print(json.dumps(pretty_json, indent=2))
    time.sleep(3)
    print("\nAdditional data\n===============")
    pprint(resp)


if __name__=="__main__":
    webinfo()
