import os
import json
import time
import itertools
import threading
import time
import sys
import requests

Magenta="\033[95m"
yellow="\033[33m"
red="\033[31m"
cyan = '\033[36m' 
green="\u001b[32m"

def eval():
    email = input('Please enter the email to be verified?\n')
    def absemail():
        api = "70259f1c443e4eb79b552b26fcc0491c"
        response = requests.get("https://emailvalidation.abstractapi.com/v1/?api_key=" +api +"&email=" + email)
        print(response.status_code)
        print(response.content)

    def reacheremail():
    
        headers = {'Authorization': '9bd3a89e-71fc-11ed-bedf-f73f2d8f00b6'}
        url = "https://api.reacher.email/v0/check_email"
        payload = {"to_email":email}
        response = requests.post(url,headers=headers, json=payload)
        print(response.text)

    def boxmail():

        url = "https://api.apilayer.com/email_verification/check?email=" +email
        payload = {}
        headers= {"apikey": "hOdi8CoLDBXWryGMAO8wcrFVNLwft7cx"}
        response = requests.request("GET", url, headers=headers, data = payload)
        status_code = response.status_code
        print(response.text)

    print(Magenta+ "All the results are using my API key which might not have enough creadit so cyhange them with your own")
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')

    t = threading.Thread(target=animate)
    t.start()
    time.sleep(10)
    done = True
    print()

    print(yellow+"______________________________________________________________________")
    print(yellow+"______________________________________________________________________")
    print(cyan+ "result of mailbox service")
    print(yellow+"______________________________________________________________________")
    print(yellow+"______________________________________________________________________")
    print(green)
    boxmail()
    print(yellow+"______________________________________________________________________")
    print(yellow+"______________________________________________________________________")
    print(cyan+ "result of reacher service")
    print(yellow+"______________________________________________________________________")
    print(yellow+"______________________________________________________________________")
    print(green)
    reacheremail()
    print(yellow+"______________________________________________________________________")
    print(yellow+"______________________________________________________________________")
    print(cyan+ "result of abstract mail service")
    print(yellow+"______________________________________________________________________")
    print(yellow+"______________________________________________________________________")
    print(green)
    absemail()
    print(yellow+"______________________________________________________________________")
    print(yellow+"______________________________________________________________________")
if __name__=="__main__":
   eval()