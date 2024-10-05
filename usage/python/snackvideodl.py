import requests
import json

endpoint = 'https://execross.com/api/v3/snackdl'
headers = {
    'apikey': 'forexecman'
}
params = {
    "url": "https://s.snackvideo.com/p/4d1JxStf",
}
try:
    response = requests.get(endpoint, params=params, headers=headers).json()
    if response['status'] == 200:
        print("Response:", json.dumps(response, indent=4))
    else:
        print("Status Code:", response['status'])

except Exception as e:
    print("An error occurred:", str(e))

"""
Response: {
    "creator": "EXECROSS",
    "ip": "61.5.71.228",
    "result": {
        "caption": "Happy sunday \ud83e\udd70More",
        "comment": "1.5K",
        "created": null,
        "fullname": "Ariel Tatum",
        "id": "5234740245276273699",
        "like": "73.8K",
        "pagelink": "https://s.snackvideo.com/p/4d1JxStf",
        "picture": "https://aws-br-pic.kwai.net/upic/2022/10/04/14/BMjAyMjEwMDQxNDAwMTJfMTUwMDAxMzcwODMzMTI2XzE1MDEwMDk2Mzk5NzUxNl8wXzM=_offn_B1c68b9dda3094be08d3465514d40ab56.webp?tag=1-1728091073-s-0-zn91gfoajh-acf1ddfa3ad1efc5",
        "share": "2.7K",
        "thumbnail": "https://aws-br-pic.kwai.net/upic/2022/10/04/14/BMjAyMjEwMDQxNDAwMTJfMTUwMDAxMzcwODMzMTI2XzE1MDEwMDk2Mzk5NzUxNl8wXzM=_offn_B1c68b9dda3094be08d3465514d40ab56.webp?tag=1-1728091073-s-0-zn91gfoajh-acf1ddfa3ad1efc5",
        "username": "ArielTatumc39668",
        "video": "https://aws-br-cdn.kwai.net/upic/2022/10/04/14/BMjAyMjEwMDQxNDAwMTJfMTUwMDAxMzcwODMzMTI2XzE1MDEwMDk2Mzk5NzUxNl8wXzM=_b_B9c86077f59bcbe11f85698e7a0021a45.mp4?tag=1-1728091073-s-0-n6g7qgvqls-7c4124400bac2629"
    },
    "status": 200
}
"""