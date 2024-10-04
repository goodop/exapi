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
            "mp3Url": "https://cdn2.meow.gs/tunnel?id=hYmrogt-FTFIcm0JfS2OH&exp=1728051688293&sig=7ALnUtpHiSJXwJNOMzvPZAUAeov69zhzj8nlous7_38&sec=zhvoIhmzO0dHvVmMz0rqsAnU2BMvg2ecK7QMbJ-NQcQ&iv=UkiBlMDeP0Z0jAXa4CV-Sg",
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
            "mp3Url": "https://cdn1.meow.gs/tunnel?id=hrxtyrAMxuqZAtYsZkAvc&exp=1728052053720&sig=JV5TpKDwdKSDm-ywUNpM7zAWPFvh23gjXSYWMzDO98c&sec=zE5zz3hXl9zo-rdPvn19jNRkdOWpbN0HBR7ZQBcuX64&iv=0UY8xZbk9P8GMimydCcDHA",
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
            "mp3Url": "https://cdn1.meow.gs/tunnel?id=3mqjgWZzLR_er68d_-q-o&exp=1728052055961&sig=bNnVDOcQNbp_VuYyVFlb2LOMMqHVP_N20wvpo-1O9zE&sec=sg3KT7axYxSQsIyfMu-MoaBRzHyxIUkkceXsIlhPobM&iv=9z7HO5w_Q5MVv__TVib5aA",
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
            "mp3Url": "https://cdn4.meow.gs/tunnel?id=cpYRKe5kwiB-vlix9peIp&exp=1728052057988&sig=hlPzSw46bHiLagFlugG3iTSl2B-O5aq5zdAEWuIvfv0&sec=mRE2f-tJYNITfTAzbMZUcRBsij7ovEdDoLP2ZRAJUxM&iv=q45rBqsjHJiv4F6OKHYtng",
            "release": "2017-12-19",
            "title": "Akad",
            "url": "https://open.spotify.com/track/3AAAGS7iM1ekDywqdYMJG2"
        }
    ],
    "status": 200
}

"""