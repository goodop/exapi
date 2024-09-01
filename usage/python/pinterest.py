import requests
import json


url = 'https://execross.com/api/v3/pinterest'
headers = {
	"apikey": "forexecman"
}
params = {
	"query":"Jakarta city"
}
datas = requests.get(url,headers=headers,params=params).json()
response = json.dumps(datas,indent=4)
print(response)



'''
Result will be:
{
    "creator": "EXECROSS",
    "ip": "125.164.1.154",
    "result": [
        "https://i.pinimg.com/736x/42/bf/cc/42bfcc8b255e4c206f95f33826c69743.jpg",
        "https://i.pinimg.com/736x/46/e2/31/46e231b15a0fbca302f34e57d4799026.jpg",
        "https://i.pinimg.com/736x/ef/8a/be/ef8abeb2b66a09a5fdae307ab9f13b4c.jpg",
        "https://i.pinimg.com/736x/c9/21/3f/c9213fce0d54c448b16c96dd2a1fbda1.jpg",
        "https://i.pinimg.com/736x/e2/77/96/e2779672fedf7a4d0f131b68039d1840.jpg"
    ],
    "status": 200
}
'''