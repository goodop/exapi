from exapi import ExecrossAPI
import json

api = ExecrossAPI(base_url='https://execross.com/api/v3', apikey='forexecman')

# Example 1: GET Proxies
proxy = api.getProxies()
print(proxy)

# Example 2: Get Appname
appnames = api.lineAppname()
print(appnames)

# Example 3: LINE Login QR Token V3
params_getqr = {
    'apikey': api.apikey,
    'appName': appnames['macOS'],
    'certificate': '',
    'proxy': proxy,
}
data = api.getQR(params_getqr)
print(data)

# Example 4: LINE Login QR V1
params_getqrv1 = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'certificate': '',
    'proxy': proxy,
}
data = api.getQRV1(params_getqrv1)
print(data)

# Example 5: LINE Login Email Token V3
params_getemail = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'certificate': '',
    'email': '',
    'password': '',
    'proxy': None,
}
data = api.getEmail(params_getemail)
print(data)

# Example 6: LINE Login Email V1
params_getemailv1 = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'certificate': '',
    'email': '',
    'password': '',
    'proxy': None,
}
data = api.getEmailV1(params_getemailv1)
print(data)

# Example 7: Adding Line Friend With Primary
params_addfriendprimary = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "uc23h7f331c8819j90fa9182db42a6e26:aWF0OiAbmkjDI5OTM2MTU....",  # change with your primary token
    'proxy': None,
    'mid': 'ufed869bc1105aedd331665d57cea407d',  # mid target
}
data = api.exampleAddFriendPrimary(params_addfriendprimary)
print(data)

# Example 8: Adding Line Friend With Secondary
params_addfriendsecondary = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'authToken': 'FG4wDOtTGT0O6uoJoHE2.eUJFsM5SCU9I+3UdHR0WuG.....',  # change with authtoken v1 or v3
    'proxy': None,
    'mid': 'ufed869bc1105aedd331665d57cea407d',  # mid target
}
data = api.exampleAddFriendSecondary(params_addfriendsecondary)
print(data)

# Example 9: Getting Story Line
params_getstory = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': 'udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....',  # change with authtoken v1 or v3
    'proxy': None,
    'mid': 'ufed869bc1105aedd331665d57cea407d'
}
data = api.getStory(params_getstory)
print(data)

# Example 10: Getting Post Line
urlp = 'https://line.me/R/home/post?userMid=ufed869bc1105aedd331665d57cea407d&postId=1172180403371226572'
params_getpost = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....",
    'proxy': None,
    'mid': urlp[36:69],
    'postId': urlp.split("postId=")[1]
}
data = api.getPost(params_getpost)
print(data)

# Example 11: Line Friend Recommendation
params_friendrecommendation = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....",  # change with your primary token or secondary token
    'proxy': None,
}
data = api.friendRecomendation(params_friendrecommendation)
print(data)

# Example 12: Line Image Message ID to URL
params_messageidtourl = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....",  # change with your primary token or secondary token
    'proxy': None,
    'messageId': "518437336376934529" # ID for images
}
data = api.messageIdToURL(params_messageidtourl)
print(data)

# Example 13: Convert Parse URL to Image Extension (.jpg)
params_convertparseurl = {
    'apikey': api.apikey,
    'parseURL': "https://obs-us.line-apps.com/myhome/h/download.nhn?oid=d4905e97265d26bd395e157ccaf63621248b311t13dccbea"
}
data = api.convertParseUrlToExtension(params_convertparseurl)
print(data)

# Example 14: Getting webp2mp4
params_webp2mp4 = {
    'apikey': api.apikey,
    'url': 'https://colinbendell.github.io/webperf/animated-gif-decode/4.webp'
}
data = api.webp2mp4(params_webp2mp4)
print(data)

# Example 15: Getting mp42gif
params_mp42gif = {
    'apikey': api.apikey,
    'url': 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4',  # URL of the MP4 video
    'start': '0',  # Start time in seconds
    'end': '10',   # End time in seconds (change to None for default behavior) / Max = 30secs
    'transparent': False  # Set to True for transparent background (original mp4 must be transparent)
}
data = api.mp42gif(params_mp42gif)
print(data)

# Example 16: Getting vid2apng
params_vid2apng = {
    'apikey': api.apikey,
    'start': '0',  # Start time in seconds
    'end': '10',   # End time in seconds (change to None for default behavior) / Max = 30secs
    'url': 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4'  # Etc.(MP4, WebM, AVI, MPEG, FLV, OGG, MOV, 3GP)
}
data = api.vid2Apng(params_vid2apng)
print(data)

# Example 17: Download smule post
params_smuledl = {
    'apikey': api.apikey,
    'url': 'https://www.smule.com/sing-recording/2732403437_4732128989'
}
data = api.smulePost(params_smuledl)
print(json.dumps(data,indent=4))


# Example 18: Download Instagram Post
params_instapost = {
    'apikey': api.apikey,
    'url': 'https://www.instagram.com/p/CMZ8rozlRXD/?igsh=MWdyaXRmaXp0bThxNg==' # Instagram Post, Reels / IGTV
}
data = api.instagramPost(params_instapost)
print(data)

# Example 19: Download Instagram Story
params_instastorie = {
    'apikey': api.apikey,
    'userid': 'jensraven9' # User ID or Story Link
}
data = api.instagramStory(params_instastorie)
print(data)

# Example 20: View Who Stalk Your Instagram
params_instastorie = {
    'apikey': api.apikey,
    'userid': 'jensraven9'
}
data = api.instaStalker(params_instastorie)
print(data)

# Example 21: Fetch Instagram Profile Details
params_igprofile = {
    'apikey': api.apikey,
    'userid': 'this.ang'
}
data = api.instagramProfileDetails(params_igprofile)
siap = json.dumps(data,indent=4)
print(siap)

# Example 22: Download Twitter/X Post
params_twitterpost = {
    'apikey': api.apikey,
    'url': 'https://twitter.com/koreanjewcrypto/status/1544681312941924352?s=20&t=7Jpn1Shcn6Kl5DG-bPzosQ'
}
data = api.downloadXpost(params_twitterpost)
print(data)

# Example 23: Download Facebook Post
params_fbpost = {
    'apikey': api.apikey,
    'url': 'https://www.facebook.com/share/r/aYSqb2vVTUrRqaTG/?mibextid=0VwfS7'
}
data = api.downloadFacebook(params_fbpost)
print(data)

# Example 24: Download Tiktok Post
params_tiktok = {
    'url': 'https://www.tiktok.com/@islamicvibes1445/video/7367927569280240901?_r=1&_t=8oUDV5F4HtB'
}
data = api.downloadTiktok(params_tiktok)
siap = json.dumps(data,indent=4)
print(siap)

# Example 25: Combine Images

# Use Files
files = [
    ('images', ('image1.jpg', open('usage/python/assets/cobrax.jpg', 'rb'), 'image/jpeg')),
    ('images', ('image2.jpg', open('usage/python/assets/th.jpeg', 'rb'), 'image/jpeg'))
]

# Use URL
data = {
    'urls': json.dumps([
        'https://images.nightcafe.studio/jobs/g9k7ET6X4eTnJMIASD9Q/g9k7ET6X4eTnJMIASD9Q--1--83vb5.jpg',
        'https://img.freepik.com/premium-photo/3d-rendering-arabian-cobra-animal-ai-generative_842224-8185.jpg'
    ])
}
filenamed = "usage/python/assets/combined.jpg" #save and renamed image result
result = api.combineImages(filenamed, files, data)
print(result)

# Example 26: Swap Face

# Example With URL
originalImage= 'https://i.ytimg.com/vi/Sw2NisGoa9c/maxres2.jpg'
faceImage = 'https://gate.execross.com/images/ki-arjuna.webp'
params = {
    'originImageURL': originalImage,
    'faceImageURL': faceImage
}
response = api.faceSwap(params=params)
print(json.dumps(response,indent=4))

# Example With Files
files = {
    'originImage': ('original_image.jpg', open('usage/python/assets/superman.webp', 'rb'), 'image/jpeg'),
    'faceImage': ('original_image.jpg', open('usage/python/assets/narji.jpeg', 'rb'), 'image/jpeg')
}
response = api.faceSwap(files=files)
print(json.dumps(response,indent=4))


# Example 27: Smule Profile
params_smuleProfile = {
    'apikey': api.apikey,
    'userId': 'NabilaNova'
}
data = api.smuleProfile(params_smuleProfile)
print(json.dumps(data,indent=4))


# Example 28: Tweet Profile
params_tweetProfile = {
    'apikey': api.apikey,
    'userId': '0xagx'
}
data = api.tweetProfile(params_tweetProfile)
print(json.dumps(data,indent=4))

# Example 29: Tiktok Profile
params_tiktokProfile = {
    'apikey': api.apikey,
    'userId': 'asking.ang'
}
data = api.tiktokProfile(params_tweetProfile)
print(json.dumps(data,indent=4))

# Example 30: Youtube Downloader
youtubedl = {
    "url": "https://youtu.be/_mp547ErQuw?si=wn9Obdk4WaT_c5Qo",  # support all youtube urls included short
}
data = api.youtubedl(youtubedl)
print(json.dumps(data,indent=4))

# Example 30: Youtube Downloader By Query
youtubeQuery = {
    "query": "Pupus Dewa 19",
}
data = api.youtubeQuery(youtubeQuery)
print(json.dumps(data,indent=4))


# Example 30: Youtube Trending Video
ytVideoTrend = {
    "region" : "ID",
    "countResult": 15 , # max 25, default 10
}
data = api.youtubeTrendingVideo(ytVideoTrend)
print(json.dumps(data,indent=4))
