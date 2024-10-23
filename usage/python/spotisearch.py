import requests
import json

endpoint = 'https://execross.com/api/v3/spotisearch'
headers = {
    'apikey': 'forexecman'
}
params = {
    'query': 'kenangan-manis'
}
try:
    response = requests.get(endpoint, params=params, headers=headers).json()
    if response['status'] == 200:
        print("Response:", json.dumps(response, indent=4))
    else:
        print("Status Code:", response['status'])

except Exception as e:
    print("An error occurred:", str(e))

'''
Response: {
    "creator": "EXECROSS",
    "ip": "182.1.67.220",
    "result": [
        {
            "album": "Walk The Talk",
            "album_artist": "Pamungkas",
            "album_name": "Kenangan Manis",
            "artist": "Pamungkas",
            "cover": "https://i.scdn.co/image/ab67616d0000b27304d4b84c6eb6b24d61bbd963",
            "mp3Url": "https://gate.execross.com/audio/8a29e80b-0c7a-4952-9ec2-b4bb3b23e5c8.mp3",
            "release": "2018-07-15",
            "title": "Kenangan Manis",
            "url": "https://open.spotify.com/track/1tS1dRfxIV9FzqdYTbJgMn"    
        }
    ],
    "status": 200
}
'''