import requests
import json
import random

base_url = 'https://execross.com/api/v3'
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey, 'Content-Type': 'application/json'})

"""
Change the endpoint with the login QR version you want:

# LOGIN QR With Authtoken V3
url = f'{base_url}/loginqr'
url2 = f'{base_url}/reqpin'
url3 = f'{base_url}/reqtoken'
Note: IPAD appname failed to get token.

# LOGIN QRV1
url = f'{base_url}/loginqrv1'
url2 = f'{base_url}/reqpinv1'
url3 = f'{base_url}/reqtokenv1'

# LOGIN QR SECURE
url = f'{base_url}/loginqrv3'
url2 = f'{base_url}/reqpinv3'
url3 = f'{base_url}/reqtokenv3'
Note: IPAD appname failed to get token.
"""

def getProxies():
    endpoint = f'{base_url}/proxies'
    response = session.get(endpoint).json()
    if response and response['status'] == 200:
       proxies = response['result']['proxies']
       return random.choice(proxies).split(':')[0]
    return None

def getAppname():
    endpoint = f'{base_url}/appnames'
    response = session.get(endpoint).json()
    if response['status'] == 200:
        return response['result']['appNames']

def getQR():
    proxy = getProxies()
    appname = getAppname()['macOS']
    print(appname)
    url = f'{base_url}/loginqr'
    url2 = f'{base_url}/reqpin'
    url3 = f'{base_url}/reqtoken'
    params = {
        'apikey': apikey,
        'appName': appname,
        'certificate': 'ed7f115c4ea1f35389d0b49357b5bd6cf2bba80809f9d60e5a8c545231fbcb86',
        'proxy': proxy,
    }
    response = session.get(url, params=params).json()
    data = json.dumps(response, indent=4)
    print("Response: ", data)
    if response['status'] == 200:
       print(f"Please scan this Qode on your smartphone: {response['result']['url']}")
       params2 = {
           'apikey': apikey,
           'session': response['result']['session']
       }
       response2 = session.get(url2, params=params2).json()
       data2 = json.dumps(response2, indent=4)
       print("Response2: ", data2)
       if 'authToken' in response2['result']:
          for key, value in response2['result'].items():
              print(f"{key}: {value}")
       else:
           print(f"please input this PIN: {response2['result']['pincode']}")
           response3 = session.get(url3, params=params2).json()
           data3 = json.dumps(response3, indent=4)
           print("response3: ", data3)
           if response3['status'] == 200:
              for key, value in response3['result'].items():
                  print(f"{key}: {value}")



getQR()

"""
# Response will be:
Response:  {
    "creator": "EXECROSS",
    "ip": "56.77.752.122",
    "proxy": "168.237.194.18",
    "result": {
        "barcode": "https://gate.execross.com/images/qrcode_1722428691.5508652.png",
        "session": "SQ504b5a4d5a727a38616648416c63313552307337386d6d6f563554367a427a65",
        "url": "https://line.me/R/au/lgn/sq/SQ504b5a4d5a727a38616648416c63313552307337386d6d6f563554367a427a65?secret=cJOKwatDulR9hm073rpdeOCByqHc2lwHxgtaYvgsMFQ%3D&e2eeVersion=1"
    },
    "status": 200
}

Response2:  {
    "creator": "EXECROSS",
    "ip": "56.77.752.122",
    "result": {
        "pincode": "571387"
    },
    "status": 200
}

Response3:  {
    "creator": "EXECROSS",
    "ip": "56.77.752.122",
    "result": {
        "authToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzYzk2NDE2Yy1hMDYwLTQ2YWMtODk1ZS05MTRiZDlkYTc1OGUiLCJhdWQiOiJMSU5FIiwiaWF0IjoxNzI0MDExMzMwLCJleHAiOjE3MjQ2MTYxMzAsInNjcCI6IkxJTkVfQ09SRSIsInJ0aWQiOiIzM2FkZmZmOS01N2EwLTQ5OGMtOTE2Ny03NDVjOGQ3MTg4NWUiLCJyZXhwIjoxNzU1NTQ3MzMwLCJ2ZXIiOiIzLjAiLCJhaWQiOiJ1MTJlOGRmNGE2ZTZjNzJlZjYyZmY3YjgzODZiZDMwNTIiLCJsc2lkIjoiYWMxMjc0YWMtMDkxYi00NzgyLTk1MTQtNGI4Y2NiNmM2YjllIiwiZGlkIjoiTk9ORSIsImN0eXBlIjoiREVTS1RPUF9NQUMiLCJjbW9kZSI6IlNFQ09OREFSWSIsImNpZCI6IjAxMDAwMDAwMDAifQ.ieQYoUj2-r1tplJRqFd8iPeAXOH95OwAZb0bqVvQqK0",
        "certificate": "ed7f115c4ea1f35389d0b49357b5bd6cf2bba80809f9d60e5a8c545231fbcb86",
        "e2eeVersion": "1",
        "keyId": "4905823",
        "privKey": "iJ1/gdLLWcMQ4/ZmhpUGZuQb0Q2Wt+QohO386JX133c=",
        "pubKey": "73qZFPG0YwcJ4PtbQ3ty5X3Itl7PRx4ZQdhUaSl+UDI=",
        "durationForRefresh": {
            "inDates": "2024-08-23 03:48:21 WIB", # Jakarta Time
            "inSeconds": 347725
        }
        "refreshToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzM2FkZmZmOS01N2EwLTQ5OGMtOTE2Ny03NDVjOGQ3MTg4NWUiLCJhdGkiOiIzYzk2NDE2Yy1hMDYwLTQ2YWMtODk1ZS05MTRiZDlkYTc1OGUiLCJhdWQiOiJMSU5FIiwicm90IjoiU1RBVElDIiwiaWF0IjoxNzI0MDExMzMwLCJleHAiOjE3NTU1NDczMzAsInNjcCI6IkxJTkVfQ09SRSIsInZlciI6IjMuMCIsImFpZCI6InUxMmU4ZGY0YTZlNmM3MmVmNjJmZjdiODM4NmJkMzA1MiIsImxzaWQiOiJhYzEyNzRhYy0wOTFiLTQ3ODItOTUxNC00YjhjY2I2YzZiOWUiLCJkaWQiOiJOT05FIiwiYXBwSWQiOiIwMTAwMDAwMDAwIn0.3YI0kVQ0Qir1jfAxmIFyxEDEkhlRNKStht5cAEjUkLk"
    },
    "status": 200
}
"""
