import requests

def exampleAddFriendSecondary():
    url = 'https://execross.com/api/v3/addfriend'
    
    params = {
        'apikey': 'forexecman',
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7', #Example Desktop win appname: 'DESKTOPWIN\t8.5.0\tWINDOWS\t10.0'
        'authToken': '', #change with authToken V1 or v3
        'proxy': '47.251.70.179',
        'mid': 'ua7dfa3ce0339d1033e83e6059f0419e1'
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f'Error: {response.status_code}')
        print(response.json())


def exampleAddFriendPrimary():
    url = 'https://execross.com/api/v3/addfriend'
    
    params = {
        'apikey': 'forexecman',
        'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
        'authToken': 'udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK..,,', #change with your primary
        'proxy': '47.251.70.179',
        'mid': 'ua7dfa3ce0339d1033e83e6059f0419e1'
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f'Error: {response.status_code}')
        print(response.json())

# Example
exampleAddFriendSecondary() #call func addfriend with secondary
exampleAddFriendPrimary() #call func addfriend with primary
