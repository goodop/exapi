import requests,json

endpoint = 'https://execross.com/api/v3/ytmusictrend'
headers = {
    'apikey': 'forexecman'
}
params = {
    "region" : "ID",
    "countResult": 10 , # max 30, default 10
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
print(json.dumps(responsed,indent=4))