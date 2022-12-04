import requests
import json
import dns.resolver
import sys

def subenum():
    print("This feature will give all the possible subdomains.\n")
    domain = input("Enter the domain: >")

    #Using whoisxmlapi 
    url = "https://subdomains.whoisxmlapi.com/api/v1?apiKey=at_jrNCEHl52VXlCpYol8eQt0me9Qub1&domainName="+domain
    response = requests.request("GET", url)
    pretty_json = json.loads(response.text)
    print (json.dumps(pretty_json, indent=3))

    #Extra checking using Kapil Kataria code
    subdomain_array = ["www","mail","ftp","localhost","webmail","smtp","pop","ns1","webdisk","ns2","cpanel","whm","autodiscover","autoconfig","m","imap","test","ns","blog","pop3","dev","www2","admin","forum","news","vpn","ns3","mail2","new","mysql","old","lists","support","mobile","mx","static","docs","beta","shop","sql","secure","demo","cp","calendar","wiki","web","media","email","images","img","www1","intranet","portal","video","sip","dns2","api","cdn","stats","dns1","ns4","www3","dns","search","staging","server","mx1","chat","wap","my","svn","mail1","sites","proxy","ads","host","crm","cms","backup","mx2","lyncdiscover","info","apps","download","remote","db","forums","store","relay","files","newsletter","app","live","owa","en","start","sms","office","exchange","ipv4"]
    subdomain_enum = []
    print("\nExtra subdomains...\n")
    for subd in subdomain_array:
        #try and except to avoid errors
        try:            
            #here dns resolve will check if the subdomain.domain is valid or not
            url = dns.resolver.resolve(f'{subd}.{domain}')
            #if subdomain.domain true then append it in subdomain_enum array
            if url:
                subdomain_enum.append(f'{subd}.{domain}')
                #if subdomain.domain in subdomain_enum array then print subdomain.domain else pass(print nothing)
                if f'{subd}.{domain}' in subdomain_enum:
                    print(f'{subd}.{domain}')
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            quit()

if __name__=="__main__":
   subenum()
