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

"""
Change the endpoint with the login email version you want:

# LOGIN EMAIL With Authtoken V3
url = f'{base_url}/loginqr'
url2 = f'{base_url}/reqpin'
url3 = f'{base_url}/reqtoken'

# LOGIN EMAILV1
url = f'{base_url}/loginqrv1'
url2 = f'{base_url}/reqpinv1'
url3 = f'{base_url}/reqtokenv1'

NOTE:
# please enabled login using password before you do this
# go settings > Account on your LINE app!

"""

def loginEmail():
    url = f'{base_url}/loginemail'
    url2 = f'{base_url}/reqemailtoken'
    params = {
        'apikey': apikey,
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
        'certificate': '',
        'email': '',
        'password': '',
        'proxy': getProxies(),
    }
    response = session.get(url, params=params).json()
    data = json.dumps(response,indent=4)
    print("Response: ", data)
    if response['status'] == 200:
        if 'authToken' in response['result']:
            data = "Login successfully"
            data += f"\nAuth Token: {response['result']['authToken']}"
            data += f"\nRefresh Token: {response['result']['refreshToken']}"
            data += f"\nCertificate: {response['result']['certificate']}"
            print(data)
        else:              
            print(f"Please input this pincode: {response['result']['pincode']}")
            params2 = {
                'apikey': apikey,
            }
            response2 = session.get(url2, params=params2).json()
            data2 = json.dumps(response2,indent=4)
            print("Response2: ", data2)
            if response2['status'] == 200:
                datax = "Login successfully"
                datax += f"\nAuth Token: {response2['result']['authToken']}"
                datax += f"\nRefresh Token: {response2['result']['refreshToken']}"
                datax += f"\nCertificate: {response2['result']['certificate']}" 
                datax += f"\nKeyID: {response2['result']['keyId']}"
                datax += f"\nPublic Key: {response2['result']['pubKey']}" 
                datax += f"\nPrivate Key: {response2['result']['privKey']}"
                datax += f"\nE2EE Version: {response2['result']['e2eeVersion']}"                
                print(datax)
            else:
                print(f"Error: {response2.get('message', 'Unknown error')}")   
    else:
        print(f"Error: {response.get('message', 'Unknown error')}")


loginEmail()

"""
# Result will be:

Response:  {
    "creator": "EXECROSS",
    "ip": "75.177.42.12",
    "proxy": "0.237.39.20",
    "result": {
        "pincode": "785887"
    },
    "status": 200
}

Response2:  {
    "creator": "EXECROSS",
    "ip": "75.177.42.12",
    "result": {
        "authToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhOWFlZThjMy00MzcyLTRmYjQtYjJhYy03ODNlMDkyYTc3ZDIiLCJhdWQiOiJMSU5FIiwiaWF0IjoxNzIyNDM5Nzg4LCJleHAiOjE3MjMwNDQ1ODgsInNjcCI6IkxJTkVfQ09SRSIsInJ0aWQiOiJmZjQzOGI5OC0yNWExLTQyZGUtODg5Mi1mYTRjNmMxZTAyOWIiLCJyZXhwIjoxNzUzOTc1Nzg4LCJ2ZXIiOiIzLjAiLCJhaWQiOiJ1MTJlOGRmNGE2ZTZjNzJlZjYyZmY3YjgzODZiZDMwNTIiLCJsc2lkIjoiMzMxNDNjZjQtZDFhOS00ZGNhLTlhZGUtYzE3Y2ZjZjg1NWViIiwiZGlkIjoiTk9ORSIsImN0eXBlIjoiREVTS1RPUF9NQUMiLCJjbW9kZSI6IlNFQ09OREFSWSIsImNpZCI6IjAxMDAwMDAwMDAifQ.zyg5ZHJclSGCJJ2o8YLnOsPhR4aBJUtcjQDlZvbWBXM",
        "certificate": "6bed8db7eb6e23ecf152f98a41e0f95294f6334f6ec45051a8801b5c00632353",
        "e2eeVersion": "1",
        "keyId": "4905823",
        "privKey": "iJ1/gdLLWcMQ4/ZmhpUGZuQb0Q2Wt+QohO386JX133c=",
        "pubKey": "73qZFPG0YwcJ4PtbQ3ty5X3Itl7PRx4ZQdhUaSl+UDI=",
        "refreshToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmZjQzOGI5OC0yNWExLTQyZGUtODg5Mi1mYTRjNmMxZTAyOWIiLCJhdGkiOiJhOWFlZThjMy00MzcyLTRmYjQtYjJhYy03ODNlMDkyYTc3ZDIiLCJhdWQiOiJMSU5FIiwicm90IjoiU1RBVElDIiwiaWF0IjoxNzIyNDM5Nzg4LCJleHAiOjE3NTM5NzU3ODgsInNjcCI6IkxJTkVfQ09SRSIsInZlciI6IjMuMCIsImFpZCI6InUxMmU4ZGY0YTZlNmM3MmVmNjJmZjdiODM4NmJkMzA1MiIsImxzaWQiOiIzMzE0M2NmNC1kMWE5LTRkY2EtOWFkZS1jMTdjZmNmODU1ZWIiLCJkaWQiOiJOT05FIiwiYXBwSWQiOiIwMTAwMDAwMDAwIn0.Oe8knxI1WrZizB2VA2q0MQARMvT7F6pP_VYqNCiZIkk"
    },
    "status": 200
}
"""
