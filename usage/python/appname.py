import requests,json

endpoint = 'https://execross.com/api/v3/appnames'
headers = {
    'apikey': 'forexecman'
}
response = requests.get(endpoint, headers=headers)
if response['status'] == 200:
    print("Response:",json.dumps(response.json(),indent=4))
else:
    print(response.content)



"""
Result wiil be:

Response: {
    "creator": "EXECROSS",
    "ip": "180.1.115.34",
    "result": {
        "appNames": {
            "android": "ANDROID\t14.11.0\tANDROID\t12.3.3772",        
            "chrome": "CHROMEOS\t3.4.0\tchrome_OS\t1",
            "ios": "IOS\t14.12.2\tiOS\t14.0.1",
            "ipad": "IOSIPAD\t14.12.2\tiPadOS\t15.7.4",
            "macOS": "DESKTOPMAC\t9.2.0\tMAC\t10.15.7",
            "windows": "DESKTOPWIN\t9.2.0\tWINDOWS\t10.0"
        },
        "appVersions": {
            "Android": "14.11.0",
            "Chrome": "3.4.0",
            "Windows": "9.2.0",
            "iOS": "14.12.2",
            "iPad": "14.12.2",
            "macOS": "9.2.0"
        }
    },
    "status": 200
}

"""