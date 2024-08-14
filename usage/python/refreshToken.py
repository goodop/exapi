import requests
import json
import random

base_url = 'https://execross.com/api/v3'
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey, 'Content-Type': 'application/json'})

def getAppname():
    endpoint = f'{base_url}/appnames'
    response = session.get(endpoint).json()
    if response['status'] == 200:
        return response['result']['appNames']

def refresh():
    refresh = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzODI5Mz....", # Change with your refresh token
    oldToken= "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2NmM3ZW...." # Change with your authToken V3
    appname = getAppname()['windows'] # Appname must desktopwin or desktopmac.
    params = {
        'appName': appname,
        'authToken': oldToken,
        'refreshToken': refresh
    }
    response = session.get(base_url + '/refreshtoken', params=params).json()
    data = json.dumps(response, indent=4)
    return data


result = refresh()
print(result)

"""
Result will be:
    "creator": "EXECROSS",
    "ip": "182.1.91.138",
    "result": {
        "newToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2NWRkZWQ2OS0xMjAyLTQ3YzItOTIwMi1jNTk4ZTU2YWFiNjYiLCJhdWQiOiJMSU5FIiwiaWF0IjoxNzIzNjIyODQyLCJleHAiOjE3MjQyMjc2NDIsInNjcCI6IkxJTkVfQ09SRSIsInJ0aWQiOiIzODI5MzcwMC1lNGE2LTRjNzYtYTBlYi0xZDI1NTY5Y2NlZTMiLCJyZXhwIjoxNzU1MTU2OTI3LCJ2ZXIiOiIzLjAiLCJhaWQiOiJ1MTJlOGRmNGE2ZTZjNzJlZjYyZmY3YjgzODZiZDMwNTIiLCJsc2lkIjoiMzdkNjQyNGEtYzYxOC00NTA3LTk1NWQtMmYwMDEyNmYxMGU0IiwiZGlkIjoiTk9ORSIsImN0eXBlIjoiREVTS1RPUF9NQUMiLCJjbW9kZSI6IlNFQ09OREFSWSIsImNpZCI6IjAxMDAwMDAwMDAifQ.D4RDX8DpF-8a-IclDik6qiu6vrLpxmepbxQTrn7WxFw"
    },
    "status": 200
}
"""