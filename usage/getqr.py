import requests
import json
import random

base_url = 'https://execross.com/api/v3'
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey, 'Content-Type': 'application/json'})

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
    print("Response: ",response)
    if response['status'] == 200:
       print(f"Please scan this Qode on your smartphone: {response['result']['url']}")
       params2 = {
           'apikey': apikey,
           'session': response['result']['session']
       }
       response2 = session.get(url2, params=params2).json()
       print("Response2: ", response2)
       if 'authToken' in response2['result']:
          for key, value in response2['result'].items():
              print(f"{key}: {value}")
       else:
           print(f"please input this PIN: {response2['result']['pin']}")
           response3 = session.get(url3, params=params2).json()
           print("response3: ", response3)
           if response3['status'] == 200:
              for key, value in response3['result'].items():
                  print(f"{key}: {value}")



getQR()

# Result will be:

Response: {
  "creator": "EXECROSS",
  "ip": "45.34.343.122",
  "proxy": "177.113.133.103",
  "result": {
    "session": "SQ36506d51696d48634e77575076567a734f57595a317a49644678397055626847",
    "url": "https://gate.execross.com/images/qrcode_1722260528.301999.png"
  },
  "status": 200
}

Response2: {
  "creator": "EXECROSS",
  "ip": "45.34.343.122",
  "result": {
    "pin": "448555"
  },
  "status": 200
}


Response3:  {
    'creator': 'EXECROSS',
    'ip': '45.34.343.122',
    'result': {
        'authToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlZDRmMDRlZi05OGU1LTQwZGItODc1YS03Yjc1YzFkMDYwZTYiLCJhdWQiOiJMSU5FIiwiaWF0IjoxNzIyMjYwODE0LCJleHAiOjE3MjI4NjU2MTQsInNjcCI6IkxJTkVfQ09SRSIsInJ0aWQiOiJiZGY3ZmQyZi0zMDQ1LTQwMTUtYjA5Ni03NGQyMDA2YTEwM2EiLCJyZXhwIjoxNzUzNzk2ODE0LCJ2ZXIiOiIzLjAiLCJhaWQiOiJ1MTJlOGRmNGE2ZTZjNzJlZjYyZmY3YjgzODZiZDMwNTIiLCJsc2lkIjoiZDg5YTJmMmYtYzg2OC00OTNjLWFkODItMzI2NTdmYzI2M2Y0IiwiZGlkIjoiTk9ORSIsImN0eXBlIjoiREVTS1RPUF9NQUMiLCJjbW9kZSI6IlNFQ09OREFSWSIsImNpZCI6IjAxMDAwMDAwMDAifQ.KxEYv0uX2Pe1o8z0rx1GnD2xOzpEAGpe9raOsPM61vY',
        'certificate': '88a895ec0d3738d49b567f79a555ec43e1443a360c5313c249106775e578c4cc',
        'e2eeVersion': '1',
        'keyId': '4905823',
        'privKey': 'iJ1/gdLLWcMQ4/ZmhpUGZuQb0Q2Wt+QohO386JX133c=',
        'pubKey': '73qZFPG0YwcJ4PtbQ3ty5X3Itl7PRx4ZQdhUaSl+UDI=',
        'refreshToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiZGY3ZmQyZi0zMDQ1LTQwMTUtYjA5Ni03NGQyMDA2YTEwM2EiLCJhdGkiOiJlZDRmMDRlZi05OGU1LTQwZGItODc1YS03Yjc1YzFkMDYwZTYiLCJhdWQiOiJMSU5FIiwicm90IjoiU1RBVElDIiwiaWF0IjoxNzIyMjYwODE0LCJleHAiOjE3NTM3OTY4MTQsInNjcCI6IkxJTkVfQ09SRSIsInZlciI6IjMuMCIsImFpZCI6InUxMmU4ZGY0YTZlNmM3MmVmNjJmZjdiODM4NmJkMzA1MiIsImxzaWQiOiJkODlhMmYyZi1jODY4LTQ5M2MtYWQ4Mi0zMjY1N2ZjMjYzZjQiLCJkaWQiOiJOT05FIiwiYXBwSWQiOiIwMTAwMDAwMDAwIn0.3t-LPUGmhO1NiInmZhL0pC-Dj0dgTZE-FNaDg-H8sSY'},
    'status': 200
}

