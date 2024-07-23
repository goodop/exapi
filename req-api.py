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

def getQR():
    url = f'{base_url}/loginqr'
    url2 = f'{base_url}/reqpin'
    url3 = f'{base_url}/reqtoken'
    params = {
        'apikey': apikey,
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
        'certificate': '90a4c5f72e26642bd769b93aa9eeae361da47a2c06e8ca237a345efbf2a86c40',
        'proxy': None,
    }
    response = session.get(url, params=params).json()
    print(response)
    
    if response and response['status'] == 200:
        params2 = {
            'apikey': apikey,
            'session': response['result']['session']
        }
        
        response2 = session.get(url2, params=params2).json()
        print(response2)
        
        if response2 and 'authToken' in response2['result']:
            print(response2)
        else:
            response3 = session.get(url3, params=params2).json()
            print(response3)
    else:
        print(f"Error: {response.get('error', 'Unknown error')}")
