import requests
import json,time

def faceSwapURL():
    url = 'https://execross.com/api/v3/swapface'
    headers = {
        "apikey": "forexecman"
    }
    originalImage= 'https://i.ytimg.com/vi/Sw2NisGoa9c/maxres2.jpg'
    faceImage = 'https://gate.execross.com/images/ki-arjuna.webp'
    params = {
        'originImageURL': originalImage,
        'faceImageURL': faceImage
    }
    response = requests.post(url, params=params,headers=headers)
    print("Response With URL:", json.dumps(response.json(),indent=4))

def faceSwapPath():
    url = 'https://execross.com/api/v3/swapface'
    headers = {
        "apikey": "forexecman"
    }
    files = {
        'originImage': ('original_image.jpg', open('assets/superman.webp', 'rb'), 'image/jpeg'),
        'faceImage': ('original_image.jpg', open('assets/narji.jpeg', 'rb'), 'image/jpeg')
    }
    response = requests.post(url, files=files,headers=headers)
    print("Response With Path:", json.dumps(response.json(),indent=4))

faceSwapURL()
time.sleep(5)
faceSwapPath()


""" Result will be:
Response With URL: {
    "creator": "EXECROSS",
    "ip": "182.1.70.14",
    "result": {
        "data": "https://gate.execross.com/images/media/_m4Z1J2lBtNEtsKP.jpg"
    },
    "status": 200
}
Response With Path: {
    "creator": "EXECROSS",
    "ip": "182.1.70.14",
    "result": {
        "data": "https://gate.execross.com/images/media/OB-mZFBlZUxADazY.jpg"
    },
    "status": 200
}
"""