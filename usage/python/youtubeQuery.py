import requests,json

endpoint = 'https://execross.com/api/v3/youtubequery'
headers = {
    'apikey': 'forexecman'
}
params = {
    "query" : "so far away",
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
print(json.dumps(responsed,indent=4))

""" 
Response will be:
{
    "creator": "EXECROSS",
    "ip": "61.5.71.228",
    "result": {
        "audioUrl": "https://rr2---sn-capm-vnae.googlevideo.com/videoplayback?expire=1728046588&ei=nJH_ZsKLJdaH6dsPlIaj-Aw&ip=172.84.183.7&id=o-ADWvyuh6QT6_gH1mBp7cOC-06-r0XKXMSekI4PzK3UXw&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=qr&mm=31%2C29&mn=sn-capm-vnae%2Csn-5hne6nzk&ms=au%2Crdu&mv=m&mvi=2&pl=24&initcwndbps=1182500&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=5322595&dur=328.840&lmt=1713023609357114&mt=1728024540&fvip=2&keepalive=yes&fexp=51300761&c=IOS&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhALv5ElPqvv4wxSohUY_8cX0qRHYpfvqgZ9yoddt4xD1uAiEAwlhg_kY78I9ThxBbG_DAMWfUiOfBgw47I8CF8hmY65Y%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ACJ0pHgwRgIhAPAf-lxjJg5xzUT79-7XCgPb-0v0Gh77N-f2tIBnDqqWAiEAgcAM-QWESSuhkD7JdZnFjeTnZOYYnfe8-xzWUuLX41c%3D",
        "author": "Avenged Sevenfold",
        "comments": "128469",
        "description": "Life Is But A Dream... https://a7x.lnk.to/libad\nTour dates and tickets: https://www.avengedsevenfold.com/tour \nA7X World exclusive merch available here: https://a7xworld.com \n\nWatch the official music video for So Far Away by Avenged Sevenfold from the album Nightmare.\n\ud83d\udd14 Subscribe to the channel: https://bit.ly/YbmcT8\u200b\n\nThis video is a raw and emotional tribute to Avenged Sevenfold's late drummer Jimmy \"The Rev\" Sullivan and celebrates the long-time friendship the band members have shared since forming A7X in Huntington Beach, CA, in 1999. The video was directed by Wayne Isham, who has directed videos for such artists as Metallica, M\u00f6tley Cr\u00fce, Megadeth, and Def Leppard, among many others. The heartfelt quality of the video is in keeping with the emotional resonance of the song, a very personal goodbye to Sullivan that appears on the band's album Nightmare.\n\nFollow A7X:\nWebsite: https://avengedsevenfold.com/ \nFacebook: https://www.facebook.com/AvengedSevenfold\nInstagram: https://www.instagram.com/avengedsevenfold\nTwitter: https://twitter.com/TheOfficialA7X \nTikTok: https://www.tiktok.com/@avengedsevenfold\nSpotify: https://spoti.fi/3Rkfded\nDiscord: https://discord.com/invite/avengedsevenfold\n\nAvenged Sevenfold is a rock band renowned for their hits \u201cSo Far Away,\u201d \u201cHail To The King,\u201d \u201cNightmare,\u201d \u201cDear God,\u201d \u201cAfterlife,\u201d \u201cA Little Piece Of Heaven,\u201d and \u201cBuried Alive.\u201d They worked with artists like Metallica, Slash, and NOFX \u2014 amassing billions of global streams and garnering critical acclaim.\n\nLyrics:\nNever feared for anything\nNever shamed but never free\nA life to heal the broken heart with all that it could\nLived a life so endlessly\nSaw beyond what others see\nI tried to heal your broken heart with all that I could\n\nWill you stay?\nWill you stay away forever?\n\nHow do I live without the ones I love?\nTime still turns the pages of the book it's burned\nPlace and time always on my mind\nI have so much to say but you're so far away\n\nPlans of what our futures hold\nFoolish lies of growing old\nIt seems we're so invincible\nThe truth is so cold\n\nA final song, a last request\nA perfect chapter laid to rest\nNow and then I try to find a place in my mind\n\nWhere you can stay\nYou can stay away forever\n\nHow do I live without the ones I love?\nTime still turns the pages of the book it's burned\nPlace and time always on my mind\nI have so much to say but you're so far away\n\nSleep tight, I'm not afraid\nThe ones that we love are here with me\nLay away a place for me\nCause as soon as I'm done I'll be on my way\nTo live eternally\n\nHow do I live without the ones I love?\nTime still turns the pages of the book it's burned\nPlace and time always on my mind\nAnd the light you left remains but it's so hard to stay\nWhen I have so much to say but you're so far away\n\nI love you\nYou were ready\nThe pain is strong and urges rise\nBut I'll see you\nWhen He lets me\nYour pain is gone, your hands untied\n\nSo far away\nAnd I need you to know\nSo far away\nAnd I need you to, need you to know\n\n#OfficialMusicVideo #AvengedSevenfold #SoFarAway #WeAreWarnerRecords",
        "duration": "05:29",
        "format": "1080p",
        "likes": "",
        "pageUrl": "https://www.youtube.com/watch?v=A7ry4cx6HfY",       
        "player": "https://www.amoyshare.com/player/?v=A7ry4cx6HfY&watch=1728024996",
        "publishedAt": "13 years ago",
        "size": "94.0MB",
        "subscribers": "6.37M",
        "thumbnail": "https://i.ytimg.com/vi/A7ry4cx6HfY/mqdefault.jpg",
        "title": "Avenged Sevenfold - So Far Away [Official Music Video]",
        "videoUrl": "https://rr2---sn-capm-vnae.googlevideo.com/videoplayback?expire=1728046590&ei=npH_ZqrtGYKE6dsPzLCYoQk&ip=172.84.183.7&id=o-AJvAwhOBKRHWzvlkEWcNeHl1g-w0MLBl3bl6GDxj4wP_&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=qr&mm=31%2C29&mn=sn-capm-vnae%2Csn-5hnednsz&ms=au%2Crdu&mv=m&mvi=2&pl=24&initcwndbps=1182500&bui=AXLXGFTSa8SvjLl3hPXYu9zh-sd7awoD_cjauSdNAQXcclPosBYQKXDYjwIBguOsU9-XN0qZ0wzbp5V0&spc=54MbxdNAvArbRPaML7Wy1D-WUMCkaAGgC3Of612_b7oh5Az7H2mL&vprv=1&svpuc=1&mime=video%2Fmp4&ns=IoqUXEx3KFZii5d0kZeODp0Q&rqh=1&gir=yes&clen=25588709&ratebypass=yes&dur=328.840&lmt=1713024274202021&mt=1728024540&fvip=3&fexp=51300760&c=WEB_CREATOR&sefc=1&txp=4538434&n=BxfE-FUJczYWYg&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ACJ0pHgwRQIhAK5uCl7MLXPQRYtKl10S_2mJFJtQzlzX8b6_iCrzfo-SAiAc07nKfCN23CYnBGzkq6dVHw2SgXH1SJMrv8QdNYXZQg%3D%3D&sig=AJfQdSswRQIgHHi6vRB8muvT5-vsEhTZ2QZtndJ3UfMXSe2Em417E00CIQC9HRA_Bo0J890Ho70MnlBwoJAjLdQWbaUqJUHeY4DJgA%3D%3D",
        "watched": "373M"
    },
    "status": 200
}
"""