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
    "bookmark": 281,
    "caption": "🚨🚨 لا تمر من هنا دون أن تساهم في توثيق مشاهد أرجل الرجال \n\nأرجو ممن تتوفر لديه صور وفيديوهات من عملية ٧ اكتوبر #طوفان_الأقصى وضعها في هذا البوست\n\n https://t.co/4kcC3vVMI4",
    "conversationId": "1841900282277716446",
    "created": "Thu Oct 03 17:57:02 +0000 2024",
    "favorite": 5038,
    "id": "1841900282277716446",
    "language": "ar",
    "media": [
      {
        "type": "image",
        "url": "https://pbs.twimg.com/media/GY9-xYSW8AAHRdV.jpg"
      },
      {
        "thumbnail": "https://pbs.twimg.com/amplify_video_thumb/1841830159424372736/img/wAXVHtF5GqOarzhP.jpg",
        "type": "video",
        "url": "https://video.twimg.com/amplify_video/1841830159424372736/vid/avc1/640x364/T6xVvBiNW7CwWJP1.mp4?tag=16"
      },
      {
        "thumbnail": "https://pbs.twimg.com/amplify_video_thumb/1841830159432679424/img/C0kmoPHY0FqbFd5Y.jpg",
        "type": "video",
        "url": "https://video.twimg.com/amplify_video/1841830159432679424/vid/avc1/640x368/0xDYkCVtho1Y8Pj4.mp4?tag=16"
      },
      {
        "type": "image",
        "url": "https://pbs.twimg.com/media/GY9-xYZXYAAhsSm.jpg"
      }
    ],
    "quote": 31,
    "reply": 67,
    "retweet": 1618,
    "tweetUrl": null,
    "userid": "1750303439857270785"
  },
  "status": 200
}

'''
