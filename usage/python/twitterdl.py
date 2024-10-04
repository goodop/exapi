import requests,json

endpoint = 'https://execross.com/api/v3/twitterdl'
headers = {
    'apikey': 'forexecman'
}
params = {
    "url" : "https://x.com/NASA/status/1822017575636603155",
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
print(json.dumps(responsed,indent=4))


'''
Response will be:

{
    "creator": "EXECROSS",
    "ip": "61.5.71.228",
    "result": {
        "bookmark": 72,
        "caption": "Last year, we brought pieces of a distant asteroid back to Earth to unlock the secrets of the universe.\n\nMeet the team that made it happen\u2014tune in for \"NASA Explorers,\" now streaming for free on NASA+: https://t.co/211IiY4fXA https://t.co/ZAgdyJ2CCy",        
        "conversationId": "1822017575636603155",
        "created": "Fri Aug 09 21:10:16 +0000 2024",
        "favorite": 2327,
        "id": "1822017575636603155",
        "language": "en",
        "media": [
            {
                "thumbnail": "https://pbs.twimg.com/media/GUkbUs3XAAEJToB.jpg",
                "type": "video",
                "url": "https://video.twimg.com/amplify_video/1822017512667586560/vid/avc1/1920x1080/Vp1COoJQ6Ler0v0W.mp4?tag=16"
            }
        ],
        "quote": 27,
        "reply": 174,
        "retweet": 380,
        "tweetUrl": null,
        "userid": "11348282"
    },
    "status": 200
}

'''
