import requests
import json
import random

base_url = 'https://execross.com/api/v3'
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey, 'Content-Type': 'application/json'})

#GET Random Proxy
def getProxies():
    url = f'{base_url}/proxies'
    response = session.get(url).json()
    if response and response['status'] == 200:
        proxies = response['result']['proxies']
        return random.choice(proxies).split(':')[0]
    return None

#GET Auth Token V3
def getQR():
    url = f'{base_url}/loginqr'
    url2 = f'{base_url}/reqpin'
    url3 = f'{base_url}/reqtoken'
    params = {
        'apikey': apikey,
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
        'certificate': '',
        'proxy': getProxies(), #use proxy for login
    }
    response = session.get(url, params=params).json()
    print(response)   
    if response and response['status'] == 200:
        params2 = {
            'apikey': apikey,
            'session': response['result']['session']
        }
        response2 = session.get(url2, params=params2).json()
        if response2 and 'authToken' in response2['result']:
            print(response2)
        else:
            response3 = session.get(url3, params=params2).json()
            print(response3)
    else:
        print(f"Error: {response.get('error', 'Unknown error')}")

#GET Auth Token V1
def getQRV1(): #Token V1
    url = f'{base_url}/loginqrv1'
    url2 = f'{base_url}/reqpinv1'
    url3 = f'{base_url}/reqtokenv1'
    params = {
        'apikey': apikey,
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
        'certificate': '',
        'proxy': None
    }
    response = session.get(url, params=params).json()
    print(response)
    if response['status'] == 200:
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

#GET Email with Auth Token V3
def getEmail():
    url = f'{base_url}/loginemail'
    url2 = f'{base_url}/reqemailtoken'
    params = {
        'apikey': apikey,
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
        'certificate': '',
        'email': '',
        'password': '',
        'proxy': None
    }
    response = session.get(url, params=params).json()
    print(response)
    if "pincode" in response['result']:
        params2 = {
            'apikey': apikey,
        }
        response2 = session.get(url2, params=params2).json()
        print(response2)

#GET Email with Auth Token V1
def getEmailV1():
    url = f'{base_url}/loginemailv1'
    url2 = f'{base_url}/reqemailtokenv1'
    params = {
        'apikey': apikey,
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
        'certificate': '',
        'email': '',
        'password': 'Askingang',
        'proxy': None
    }
    response = session.get(url, params=params).json()
    print(response)
    if "pincode" in response['result']:
        params2 = {
            'apikey': apikey,
        }
        response2 = session.get(url2, params=params2).json()
        print(response2)

def exampleAddFriendPrimary():
    url = f'{base_url}/addfriend'
    params = {
        'apikey': apikey,
        'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
        'authToken': "ugh23h7f331c8819j90fa9182db42a6e26:aWF0OiAbm....", #change with your primary token
        'proxy': None,
        'mid':'' #mid target
    }
    response = session.get(url, params=params).json()
    print(response)

def exampleAddFriendSecondary():
    url = f'{base_url}/addfriend'
    params = {
        'apikey': apikey,
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
        'authToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ODIxOTc5MC1kYWU3LTRjM2YtOWIzZC05OWRhZmU4MTdl...', # change with authtoken v1 or v3
        'proxy': None,
        'mid': '' #mid target
    }
    response = session.get(url, params=params).json()
    print(response)


#GET Friend Recomendation
def friendRecomendation():
    url = f'{base_url}/friendrecomendation'
    params = {
        'apikey': apikey,
        'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772', #change with secondary AppName if you want use secondary token
        'authToken': "uc23h7f331c8819j90fa9182db42a6e26:aWF0Oi......", #change with your primary token  or secondary Token
        'proxy': None,
    }
    response = session.get(url, params=params).json()
    print(response)

#Download Story
def getStory():
    url = f'{base_url}/linestory'
    params = {
        'apikey': apikey,
        'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772', #change with secondary AppName if you want use Token V3
        'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:F0OiAxMDI5OTM2NTkxMDAK...", #change with your primary token or auth token V3
        'proxy': None,
        'mid': 'ufed869bc1105aedd331665d57cea407d'
    }
    response = session.get(url, params=params).json()
    print(response)

#Download Post
def getPost():
    url = f'{base_url}/linepost'
    urlp = 'https://line.me/R/home/post?userMid=ufed869bc1105aedd331665d57cea407d&postId=1172180403371226572'
    params = {
        'apikey': apikey,
        'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772', #change with secondary AppName if you want use token V3
        'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:F0OiAxMDI5OTM2NTkxMDAK...", #change with your primary token or auth token V3
        'proxy': None,
        'mid': urlp[36:69],
        'postId': urlp.split("postId=")[1]
    }
    response = session.get(url, params=params).json()
    print(response)

if __name__ == '__main__':
    print("Example 1: Getting QR Code")
    getQR()

    print("\nExample 2: Getting Email")
    getEmail()

    print("\nExample 3: Adding Friend")
    addFriend()
