import requests,json

endpoint = 'https://execross.com/api/v3/ytvideotrend'
headers = {
    'apikey': 'forexecman'
}
params = {
    "region" : "ID",
    "countResult": 15 , # max 25, default 10
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
print(json.dumps(responsed,indent=4))
