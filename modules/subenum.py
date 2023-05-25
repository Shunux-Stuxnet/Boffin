import requests
import json
import dns.resolver

DEFAULT_API_KEY = 'at_vGmy0FhsoYe4Pf7knT9qmwrARCnP0'

def get_user_api_key():
    print("This feature will give all the possible subdomains.\n")
    api_key = input("Enter your API key (or press Enter to use the default key): ")
    if api_key:
        return api_key
    else:
        return DEFAULT_API_KEY

def subenum():
    api_key = get_user_api_key()
    domain = input("Enter the domain: >")

    url = f"https://subdomains.whoisxmlapi.com/api/v1?apiKey={api_key}&domainName={domain}"
    response = requests.request("GET", url)
    pretty_json = json.loads(response.text)
    print (json.dumps(pretty_json, indent=3))

    subdomain_array = ["www","mail","ftp","localhost","webmail","smtp","pop","ns1","webdisk","ns2","cpanel","whm","autodiscover","autoconfig","m","imap","test","ns","blog","pop3","dev","www2","admin","forum","news","vpn","ns3","mail2","new","mysql","old","lists","support","mobile","mx","static","docs","beta","shop","sql","secure","demo","cp","calendar","wiki","web","media","email","images","img","www1","intranet","portal","video","sip","dns2","api","cdn","stats","dns1","ns4","www3","dns","search","staging","server","mx1","chat","wap","my","svn","mail1","sites","proxy","ads","host","crm","cms","backup","mx2","lyncdiscover","info","apps","download","remote","db","forums","store","relay","files","newsletter","app","live","owa","en","start","sms","office","exchange","ipv4","learn", "edu", "course", "class", "study", "schooling", "knowledge", "scholar", "tutor", "exam",    "wellness", "fit", "medical", "care", "clinic", "therapy", "heal", "mindbody", "nutrition", "yoga",    "paygate", "cash", "checkout", "banking", "invoice", "wallet", "coin", "fintech", "moneyflow", "card",    "secure", "firewall", "encrypt", "defend", "hackproof", "auth", "security", "privacy", "lock", "shield",    "chain", "crypto", "smart", "token", "ledger", "block", "decentral", "dapp", "crypto", "wallet",    "adult", "pleasure", "erotic", "sensual", "desire", "passion", "intimate", "naughty", "tempt", "seduce",    "web", "online", "net", "site", "page", "link", "surf", "browse", "connect", "host",    "tech", "code", "geek", "hacker", "software", "robot", "ai", "cloud", "data", "device",    "ad", "campaign", "seo", "analytics", "brand", "buzz", "market", "promo", "social", "target",    "game", "play", "gamer", "console", "joystick", "score", "quest", "level", "eSports", "arcade",    "music", "sound", "rhythm", "melody", "tune", "song", "audio", "band", "concert", "jam",    "trip", "voyage", "explore", "adventure", "journey", "roam", "wander", "passport", "vacation", "itinerary","food", "eats", "taste", "yum", "delicious", "savor", "crave", "recipe", "cook", "restaurant",    "fashion", "style", "trend", "chic", "couture", "wardrobe", "glam", "runway", "model", "boutique",    "sports", "athlete", "fitness", "game", "stadium", "team", "play", "champion", "fan", "victory",    "art", "paint", "canvas", "gallery", "creative", "draw", "exhibit", "sculpt", "design", "craft",    "photo", "snap", "capture", "lens", "shoot", "picture", "frame", "album", "gallery", "portrait",    "money", "invest", "wealth", "stock", "fund", "portfolio", "capital", "savings", "economy", "bank",    "news", "headline", "press", "media", "journal", "report", "update", "article", "breaking", "coverage",    "science", "research", "lab", "experiment", "discovery", "theory", "data", "analysis", "innovation", "tech",    "fitness", "gym", "workout", "strength", "health", "active", "shape", "exercise", "wellness", "train",    "diy", "craft", "build", "create", "handmade", "project", "tools", "workshop", "maker", "repair"]
    subdomain_enum = []
    print("\nExtra subdomains...\n")
    for subd in subdomain_array:
        try:            
            url = dns.resolver.resolve(f'{subd}.{domain}')
            if url:
                subdomain_enum.append(f'{subd}.{domain}')
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
