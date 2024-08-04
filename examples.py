from exapi import ExecrossAPI
import json

api = ExecrossAPI(base_url='https://execross.com/api/v3', apikey='forexecman')

# Example 1: LINE Login QR Token V3
proxy = api.getProxies()
params_getqr = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'certificate': '',
    'proxy': proxy,
}
data = api.getQR(params_getqr)
print(data)

# Example 2: LINE Login QR V1
params_getqrv1 = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'certificate': '',
    'proxy': proxy,
}
data = api.getQRV1(params_getqrv1)
print(data)

# Example 3: LINE Login Email Token V3
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

# Example 4: LINE Login Email V1
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

# Example 5: Adding Line Friend With Primary
params_addfriendprimary = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "uc23h7f331c8819j90fa9182db42a6e26:aWF0OiAbmkjDI5OTM2MTU2MDAK....",  # change with your primary token
    'proxy': None,
    'mid': 'ufed869bc1105aedd331665d57cea407d',  # mid target
}
data = api.exampleAddFriendPrimary(params_addfriendprimary)
print(data)

# Example 6: Adding Line Friend With Secondary
params_addfriendsecondary = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'authToken': 'FG4wDOtTGT0O6uoJoHE2.eUJFsM5SCU9I+3UdHR0WuG.....',  # change with authtoken v1 or v3
    'proxy': None,
    'mid': 'ufed869bc1105aedd331665d57cea407d',  # mid target
}
data = api.exampleAddFriendSecondary(params_addfriendsecondary)
print(data)

# Example 7: Getting Story Line
params_getstory = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': 'udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....',  # change with authtoken v1 or v3
    'proxy': None,
    'mid': 'ufed869bc1105aedd331665d57cea407d'
}
data = api.getStory(params_getstory)
print(data)

# Example 8: Getting Post Line
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

# Example 9: Line Friend Recommendation
params_friendrecommendation = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....",  # change with your primary token or secondary token
    'proxy': None,
}
data = api.friendRecomendation(params_friendrecommendation)
print(data)

# Example 10: Line Image Message ID to URL
params_messageidtourl = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....",  # change with your primary token or secondary token
    'proxy': None,
    'messageId': "518437336376934529" # ID for images
}
data = api.messageIdToURL(params_messageidtourl)
print(data)

# Example 11: Convert Parse URL to Image Extension (.jpg)
params_convertparseurl = {
    'apikey': api.apikey,
    'parseURL': "https://obs-us.line-apps.com/myhome/h/download.nhn?oid=d4905e97265d26bd395e157ccaf63621248b311t13dccbea"
}
data = api.convertParseUrlToExtension(params_convertparseurl)
print(data)

# Example 12: Getting webp2mp4
params_webp2mp4 = {
    'apikey': api.apikey,
    'url': 'https://colinbendell.github.io/webperf/animated-gif-decode/4.webp'
}
data = api.webp2mp4(params_webp2mp4)
print(data)

# Example 13: Getting mp42gif
params_mp42gif = {
    'apikey': api.apikey,
    'url': 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4',  # URL of the MP4 video
    'start': '0',  # Start time in seconds
    'end': '10',   # End time in seconds (change to None for default behavior) / Max = 30secs
    'transparent': False  # Set to True for transparent background (original mp4 must be transparent)
}
data = api.mp42gif(params_mp42gif)
print(data)

# Example 14: Getting vid2apng
params_vid2apng = {
    'apikey': api.apikey,
    'start': '0',  # Start time in seconds
    'end': '10',   # End time in seconds (change to None for default behavior) / Max = 30secs
    'url': 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4'  # Etc.(MP4, WebM, AVI, MPEG, FLV, OGG, MOV, 3GP)
}
data = api.vid2Apng(params_vid2apng)
print(data)

# Example 15: Download smule post
params_smuledl = {
    'apikey': api.apikey,
    'url': 'https://www.smule.com/recording/vita-alvia-singkong-dan-keju-dj-remix/489839279_4906184190?channel=Copy-Link'
}
data = api.smulePost(params_smuledl)
print(data)

# Example 16: Download Instagram Post
params_instapost = {
    'apikey': api.apikey,
    'url': 'https://www.instagram.com/p/CMZ8rozlRXD/?igsh=MWdyaXRmaXp0bThxNg==' # Instagram Post, Reels / IGTV
}
data = api.instagramPost(params_instapost)
print(data)

# Example 17: Download Instagram Story
params_instastorie = {
    'apikey': api.apikey,
    'userid': 'jensraven9' # User ID or Story Link
}
data = api.instagramStory(params_instastorie)
print(data)

# Example 18: View Who Stalk Your Instagram
params_instastorie = {
    'apikey': api.apikey,
    'userid': 'jensraven9'
}
data = api.instaStalker(params_instastorie)
print(data)

# Example 19: Fetch Instagram Profile Details
# params_igprofile = {
#     'apikey': api.apikey,
#     'userid': 'this.ang'
# }
# data = api.instagramProfileDetails(params_igprofile)
# siap = json.dumps(data,indent=4)
# print(siap)

# # Example 20: Download Twitter/X Post
# params_twitterpost = {
#     'apikey': api.apikey,
#     'url': 'https://x.com/NASA/status/1816862466816496101?t=VAW_bUjPQgCKbxqrovVa6A&s=19'
# }
# data = api.downloadXpost(params_twitterpost)
# print(data)

# # Example 21: Download Facebook Post
# params_fbpost = {
#     'apikey': api.apikey,
#     'url': 'https://www.facebook.com/share/r/aYSqb2vVTUrRqaTG/?mibextid=0VwfS7'
# }
# data = api.downloadFacebook(params_fbpost)
# print(data)

# # Example 22: Download Tiktok Post
# params_tiktok = {
#     'apikey': api.apikey,
#     'url': 'https://www.tiktok.com/@islamicvibes1445/video/7367927569280240901?_r=1&_t=8oUDV5F4HtB'
# }
# data = api.downloadTiktok(params_tiktok)
# siap = json.dumps(data,indent=4)
# print(siap)
