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

def getQR():
    proxy = getProxies()
    url = f'{base_url}/loginqr'
    url2 = f'{base_url}/reqpin'
    url3 = f'{base_url}/reqtoken'
    params = {
        'apikey': apikey,
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
        'certificate': '',
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

response3:  {
    "creator": "EXECROSS",
    "ip": "56.77.752.122",
    "result": {
        "authToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZWVhMzM5Mi1hOGNiLTRiZGUtOTQ1Yy0yZWIzODhhYWE2NTgiLCJhdWQiOiJMSU5FIiwiaWF0IjoxNzIyNDI4NzI5LCJleHAiOjE3MjMwMzM1MjksInNjcCI6IkxJTkVfQ09SRSIsInJ0aWQiOiJhMDY4YjVjMi01MDE0LTQ2MjgtYmQ3NS03ZmZkYmMyYjc2ZGQiLCJyZXhwIjoxNzUzOTY0NzI5LCJ2ZXIiOiIzLjAiLCJhaWQiOiJ1ZmVkODY5YmMxMTA1YWVkZDMzMTY2NWQ1N2NlYTQwN2QiLCJsc2lkIjoiMGUyYzIyYWMtYmU3Yy00YTY0LTg2ZGItYzJkNDIzY2VkNTQwIiwiZGlkIjoiTk9ORSIsImN0eXBlIjoiREVTS1RPUF9NQUMiLCJjbW9kZSI6IlNFQ09OREFSWSIsImNpZCI6IjAxMDAwMDAwMDAifQ.JN3Q2MeoZwEYwvYryymiSFgkGD8RGjgwLKpZiP_MgjE",
        "certificate": "b94016ced76d63b3c0da47e8cb51e58e0bf6e982be57e9de21f0f0530d24f883",
        "e2eeVersion": "1",
        "keyId": "4869324",
        "privKey": "4MctBnCsF7lzvPY587Ar0B8+KwlWRpLV15CGaeJPtE0=",
        "pubKey": "dId6SdQAnP1JdIDRcjFV+a45DR6662XdS1tkRaUZBFk=",
        "refreshToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhMDY4YjVjMi01MDE0LTQ2MjgtYmQ3NS03ZmZkYmMyYjc2ZGQiLCJhdGkiOiI2ZWVhMzM5Mi1hOGNiLTRiZGUtOTQ1Yy0yZWIzODhhYWE2NTgiLCJhdWQiOiJMSU5FIiwicm90IjoiU1RBVElDIiwiaWF0IjoxNzIyNDI4NzI5LCJleHAiOjE3NTM5NjQ3MjksInNjcCI6IkxJTkVfQ09SRSIsInZlciI6IjMuMCIsImFpZCI6InVmZWQ4NjliYzExMDVhZWRkMzMxNjY1ZDU3Y2VhNDA3ZCIsImxzaWQiOiIwZTJjMjJhYy1iZTdjLTRhNjQtODZkYi1jMmQ0MjNjZWQ1NDAiLCJkaWQiOiJOT05FIiwiYXBwSWQiOiIwMTAwMDAwMDAwIn0.aQtA12ELks3vsJx1U0K8yJ7s6HhhD6fYjQKUXz4zQLc"
    },
    "status": 200
}

