import requests
import json

endpoint = 'https://execross.com/api/v3/githubdl'
headers = {
    'apikey': 'forexecman',
    "Content-Type": "application/json"
}
data = {
    "gitUrl": "https://github.com/goodop/exapi.git"
}

response = requests.post(endpoint, json=data, headers=headers).json()
print("Response:", json.dumps(response, indent=4))
