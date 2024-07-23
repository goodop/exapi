import requests
import json
import random

base_url = 'https://execross.com/api/v3'
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey, 'Content-Type': 'application/json'})


def getProxies():
    url = f'{base_url}/proxies'
    response = session.get(url).json()
    if response and response['status'] == 200:
        proxies = response['result']['proxies']
        return random.choice(proxies).split(':')[0]
    return None


