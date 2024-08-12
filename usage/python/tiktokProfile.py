import requests,json

endpoint = 'https://execross.com/api/v3/tiktokprofile'
headers = {
    'apikey': 'forexecman'
}
params = {
    "userId" : "asking.ang",
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
if responsed['status'] == 200:
    print("Response:",json.dumps(responsed,indent=4))
else:
    print(responsed)

'''
Result will be:

Response: {
    "creator": "EXECROSS",
    "ip": "182.1.80.151",
    "result": {
        "stats": {
            "diggCount": 0,
            "followerCount": 503,
            "followingCount": 4,
            "heart": 7,
            "heartCount": 7,
            "videoCount": 8
        },
        "user": {
            "avatarLarger": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/2ef0f943669bd6672a6131315b38cf31~c5_1080x1080.jpeg?lk3s=a5d48078&nonce=75397&refresh_token=5a738613623ebd66cd1d3f8e0b6a13d7&x-expires=1723575600&x-signature=UkNjOG48jE3KnAsxIcbYudc%2FsMI%3D&shp=a5d48078&shcp=2472a6c6",
            "avatarMedium": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/2ef0f943669bd6672a6131315b38cf31~c5_720x720.jpeg?lk3s=a5d48078&nonce=95242&refresh_token=e930933dde4063cd6a2eeeae821d10ba&x-expires=1723575600&x-signature=ozSavB4Ry5JyB15oNMlPQy9ofUw%3D&shp=a5d48078&shcp=2472a6c6",
            "avatarThumb": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/2ef0f943669bd6672a6131315b38cf31~c5_100x100.jpeg?lk3s=a5d48078&nonce=35459&refresh_token=156a949a65062ed624635b0abfe94e85&x-expires=1723575600&x-signature=uHcIaiwdEAAdBymRjRwWb1rdYKc%3D&shp=a5d48078&shcp=2472a6c6",
            "commentSetting": null,
            "duetSetting": null,
            "ftc": false,
            "id": "7161367253526217755",
            "ins_id": "",
            "isADVirtual": false,
            "isUnderAge18": false,
            "nickname": "asking.ang",
            "openFavorite": false,
            "privateAccount": false,
            "relation": 0,
            "secUid": "MS4wLjABAAAA7dla7b2cQ9YB1GQnz7KuXDKEf37BncUIue2lh9dgoL7PjBjmofbkPB9DgR67Ki7f",
            "secret": false,
            "signature": "https://ang.execross.com",
            "stitchSetting": null,
            "twitter_id": "",
            "uniqueId": "asking.ang",
            "verified": false,
            "youtube_channel_id": "",
            "youtube_channel_title": ""
        }
    },
    "status": 200
}

'''