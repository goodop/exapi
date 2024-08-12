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
    "ip": "182.1.80.151",
    "result": {
        "bookmark_count": 67,
        "bookmarked": false,
        "conversation_id_str": "1822017575636603155",
        "created_at": "Fri Aug 09 21:10:16 +0000 2024",
        "favorite_count": 2509,
        "favorited": false,
        "full_text": "Last year, we brought pieces of a distant asteroid back to Earth to unlock the secrets of the universe.\n\nMeet the team that made it happen\u2014tune in for \"NASA Explorers,\" now streaming for free on NASA+: https://t.co/211IiY4fXA https://t.co/ZAgdyJ2CCy",
        "id_str": "1822017575636603155",
        "is_quote_status": false,
        "lang": "en",
        "media": {
            "photo": {
                "url": ""
            },
            "video": {
                "url": "https://video.twimg.com/amplify_video/1822017512667586560/vid/avc1/1920x1080/Vp1COoJQ6Ler0v0W.mp4?tag=16"
            }
        },
        "note_tweet": null,
        "possibly_sensitive": false,
        "possibly_sensitive_editable": true,
        "quote_count": 21,
        "reply_count": 161,
        "retweet_count": 331,
        "retweeted": false,
        "user_id_str": "11348282"
    },
    "status": 200
}


error:


{
    "message": "Failed to fetch data\nplease try again.",
    "status": 403
}

# Retry

'''
