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

"""
Response: {
    "creator": "EXECROSS",
    "ip": "182.1.91.138",
    "result": {
        "download_url": "http://execross.com/api/v3/download/e5a580c1-07f7-4ef2-9111-45dda24b8c39-exapi.zip",
        "expired_url": "2024-08-14 15:58:43 WIB",
        "source_url": "https://github.com/goodop/exapi.git"
    },
    "status": 200
}
"""