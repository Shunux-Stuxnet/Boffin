import requests
import json
wapapi = 'wgYvzU4pKd7i4UMcSPYTaKCjk2I1ILm7gKMbEHlj'
def webinfo():
    list_response = []
    web = input("Enter the website you want to know about? > ")
    url = 'https://api.wappalyzer.com/lookup/v2/?urls=' + web + '&sets=meta,locale,security,trackers,events'
    headers = {'x-api-key' : wapapi}
    r = requests.get(url, headers=headers)
    list_response.append(r.json())
    pretty_json = json.loads(r.text)
    print (json.dumps(pretty_json, indent=2))
if __name__=="__main__":
   webinfo()