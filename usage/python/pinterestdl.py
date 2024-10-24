import requests
import json


url = 'https://execross.com/api/v3/pinterestdl'
headers = {
	"apikey": "YOUR APIKEY"
}
params = {
	"urls":"https://pin.it/3XyloCaYb"
}
datas = requests.get(url,headers=headers,params=params).json()
response = json.dumps(datas,indent=4)
print(response)

'''

#IMAGE/VIDEO RESULT

{
    "creator": "EXECROSS",
    "ip": "36.74.51.197",
    "result": {
        "follower": "",
        "media": [
            {
                "thumbnail": "https://i.pinimg.com/originals/d2/2f/f2/d22ff2e893e8522b2f4cd0becbb12b17.jpg",
                "type": "video",
                "url": "https:https://v1.pinimg.com/videos/mc/720p/c0/62/89/c0628922d4c45a591ba8c211afdc157d.mp4"
            },
            {
                "type": "image/jpg",
                "url": "https://i.pinimg.com/originals/d2/2f/f2/d22ff2e893e8522b2f4cd0becbb12b17.jpg"
            }
        ],
        "profileUrl": "https://i.pinimg.com/75x75_RS/fd/39/04/fd3904e94db0d7437ddd5b9e9c3012bb.jpg",
        "title": "Newspaper Slideshow - After Effects",
        "username": "Talent Touch"
    },
    "status": 200
}



# GIF RESULT

{
    "creator": "EXECROSS",
    "ip": "36.74.51.197",
    "result": {
        "follower": "4.8M followers",
        "media": [
            {
                "type": "gif",
                "url": "https://i.pinimg.com/originals/96/c8/8b/96c88b42028685d8cab8c083595333f6.gif"
            }
        ],
        "profileUrl": "https://i.pinimg.com/75x75_RS/74/8f/40/748f40a1dc49bba2298936edbc05fde1.jpg",
        "title": "Art Adventure Time",
        "username": "imgur"
    },
    "status": 200
}
'''