import requests
import json


url = 'https://execross.com/api/v3/pinterestdl'
headers = {
	"apikey": "YOUR APIKEY"
}
params = {
	"urls":"https://pin.it/3XyloCaYb"
}
datas = requests.get(url,headers=headers,params=params).json()
response = json.dumps(datas,indent=4)
print(response)

'''
{
    "creator": "EXECROSS",
    "ip": "36.74.51.197",
    "result": {
        "follower": "4.8M followers",
        "gif": "https://i.pinimg.com/originals/96/c8/8b/96c88b42028685d8cab8c083595333f6.gif",
        "image": "",
        "profileUrl": "https://i.pinimg.com/75x75_RS/74/8f/40/748f40a1dc49bba2298936edbc05fde1.jpg",
        "title": "Art Adventure Time",
        "username": "imgur",
        "video": ""
    },
    "status": 200
}
'''