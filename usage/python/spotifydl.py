import requests
import json

endpoint = 'https://execross.com/api/v3/spotifydl'
headers = {
    'apikey': 'forexecman'
}
params = {
    "url": "https://open.spotify.com/playlist/3yuRqnBlZHR0f9dm5zZrnk?si=BRabR9FMS2qZIba_B0oJoA",
    # Example of a track URL: https://open.spotify.com/track/6VggIDYOnf9C8fJVcMpxAu?si=M7k2YF_mR62EvUdbHuqMfw
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
Response will be:

#TRACK 
Response: {
    "creator": "EXECROSS",
    "ip": "61.5.71.228",
    "result": [
        {
            "album": "Kerajaan Cinta",
            "album_artist": "Dewa 19",
            "album_name": "Kangen",
            "artist": "Dewa 19",
            "cover": "https://i.scdn.co/image/ab67616d0000b27370ea19fd1f517d40b9c01c0d",
            "mp3Url": "https://gate.execross.com/audio/dad0baf3-2d5a-4e54-9336-b1776daad5dd.mp3",
            "release": "2007-12-03",
            "title": "Kangen",
            "url": "https://open.spotify.com/track/6VggIDYOnf9C8fJVcMpxAu"
        }
    ],
    "status": 200
}


#PLAYLIST
for playlist i just take 5 song result for avoid spamming.
any idea?

Response: {
    "creator": "EXECROSS",
    "ip": "61.5.71.228",
    "result": [
        {
            "album": "f\u00e1bula",
            "album_artist": "angcode",
            "album_name": "Galau",
            "artist": "Mahalini",
            "cover": "https://i.scdn.co/image/ab67616d00001e026f713eb92ebf7ca05a562542",
            "mp3Url": "https://gate.execross.com/audio/d012a25f-afeb-4927-9aa4-735c85f330fb.mp3",
            "release": null,
            "title": "Bawa Dia Kembali",
            "url": "https://open.spotify.com/track/25M9piWxSsq0xLcjQW5yz6"
        },
        {
            "album": "Dunia Batas",
            "album_artist": "",
            "album_name": "",
            "artist": "Payung Teduh",
            "cover": "",
            "mp3Url": "https://gate.execross.com/audio/003f8816-ee36-42b6-87e9-db4eabbd0816.mp3",
            "release": "2014-11-04",
            "title": "Untuk Perempuan Yang Sedang Di Pelukan",
            "url": "https://open.spotify.com/track/0urpBLpcm6DOGzs86rcKd8"
        },
        {
            "album": "Ruang Tunggu",
            "album_artist": "",
            "album_name": "",
            "artist": "Payung Teduh",
            "cover": "",
            "mp3Url": "https://gate.execross.com/audio/89aba52a-d6f9-45b1-9a40-8d372bd66854.mp3",
            "release": "2017-12-19",
            "title": "Akad",
            "url": "https://open.spotify.com/track/3AAAGS7iM1ekDywqdYMJG2"
        }
    ],
    "status": 200
}
"""