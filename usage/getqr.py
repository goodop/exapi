import requests
import json
import random

base_url = 'https://execross.com/api/v3'  # Corrected base URL
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey, 'Content-Type': 'application/json'})

def getProxies():
    endpoint = f'{base_url}/proxies'
    response = session.get(endpoint).json()  # Changed to GET request
    if response and response['status'] == 200:
       proxies = response['result']['proxies']
       return random.choice(proxies).split(':')[0]
    return None

def getQR():
    url = f'{base_url}/loginqr'
    url2 = f'{base_url}/reqpin'
    url3 = f'{base_url}/reqtoken'
    proxy = getProxies()
    params = {
        'apikey': apikey,
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
        'certificate': '',
        'proxy': proxy
    }
    response = session.get(url, params=params).json()
    if response['status'] == 200:
       print(f"Please scan this Qode on your smartphone: {response['result']['url']}")
       params2 = {
           'apikey': apikey,
           'session': response['result']['session']
       }
       response2 = session.get(url2, params=params2).json()
       if 'authToken' in response2['result']:
          for key, value in response2['result'].items():
              print(f"{key}: {value}")
       else:
           print(f"please input this PIN: {response2['result']['pin']}")
           response3 = session.get(url3, params=params2).json()
           if response3['status'] == 200:
              for key, value in response3['result'].items():
                  print(f"{key}: {value}")

# Example call
getQR()
