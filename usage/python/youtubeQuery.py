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
    "ip": "182.1.87.23",
    "result": {
        "author": "Avenged Sevenfold",
        "comments": "127790",
        "description": "Life Is But A Dream... https://a7x.lnk.to/libad\nTour dates and tickets: https://www.avengedsevenfold.com/tour \nA7X World exclusive merch available here: https://a7xworld.com \n\nWatch the official music video for So Far Away by Avenged Sevenfold from the album Nightmare.\n\ud83d\udd14 Subscribe to the channel: https://bit.ly/YbmcT8\u200b\n\nThis video is a raw and emotional tribute to Avenged Sevenfold's late drummer Jimmy \"The Rev\" Sullivan and celebrates the long-time friendship the band members have shared since forming A7X in Huntington Beach, CA, in 1999. The video was directed by Wayne Isham, who has directed videos for such artists as Metallica, M\u00f6tley Cr\u00fce, Megadeth, and Def Leppard, among many others. The heartfelt quality of the video is in keeping with the emotional resonance of the song, a very personal goodbye to Sullivan that appears on the band's album Nightmare.\n\nFollow A7X:\nWebsite: https://avengedsevenfold.com/ \nFacebook: https://www.facebook.com/AvengedSevenfold\nInstagram: https://www.instagram.com/avengedsevenfold\nTwitter: https://twitter.com/TheOfficialA7X \nTikTok: https://www.tiktok.com/@avengedsevenfold\nSpotify: https://spoti.fi/3Rkfded\nDiscord: https://discord.com/invite/avengedsevenfold\n\nAvenged Sevenfold is a rock band renowned for their hits \u201cSo Far Away,\u201d \u201cHail To The King,\u201d \u201cNightmare,\u201d \u201cDear God,\u201d \u201cAfterlife,\u201d \u201cA Little Piece Of Heaven,\u201d and \u201cBuried Alive.\u201d They worked with artists like Metallica, Slash, and NOFX \u2014 amassing billions of global streams and garnering critical acclaim.\n\nLyrics:\nNever feared for anything\nNever shamed but never free\nA life to heal the broken heart with all that it could\nLived a life so endlessly\nSaw beyond what others see\nI tried to heal your broken heart with all that I could\n\nWill you stay?\nWill you stay away forever?\n\nHow do I live without the ones I love?\nTime still turns the pages of the book it's burned\nPlace and time always on my mind\nI have so much to say but you're so far away\n\nPlans of what our futures hold\nFoolish lies of growing old\nIt seems we're so invincible\nThe truth is so cold\n\nA final song, a last request\nA perfect chapter laid to rest\nNow and then I try to find a place in my mind\n\nWhere you can stay\nYou can stay away forever\n\nHow do I live without the ones I love?\nTime still turns the pages of the book it's burned\nPlace and time always on my mind\nI have so much to say but you're so far away\n\nSleep tight, I'm not afraid\nThe ones that we love are here with me\nLay away a place for me\nCause as soon as I'm done I'll be on my way\nTo live eternally\n\nHow do I live without the ones I love?\nTime still turns the pages of the book it's burned\nPlace and time always on my mind\nAnd the light you left remains but it's so hard to stay\nWhen I have so much to say but you're so far away\n\nI love you\nYou were ready\nThe pain is strong and urges rise\nBut I'll see you\nWhen He lets me\nYour pain is gone, your hands untied\n\nSo far away\nAnd I need you to know\nSo far away\nAnd I need you to, need you to know\n\n#OfficialMusicVideo #AvengedSevenfold #SoFarAway #WeAreWarnerRecords",
        "duration": "05:29",
        "likes": "",
        "media": {
            "audio": "https://rr1---sn-hp57ynly.googlevideo.com/videoplayback?expire=1723507743&ei=v0-6Zpr1J7CAkucP7rrM4QM&ip=2a05%3A9405%3A0%3A4%3Ad020%3A3%3A0%3A4f50&id=o-ALyHM3FkoX9up_lX2iDj-iUO51kpYwiYtRG7WMPDOIe2&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=qr&mm=31%2C29&mn=sn-hp57ynly%2Csn-hp57knds&ms=au%2Crdu&mv=m&mvi=1&pl=32&initcwndbps=741250&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=5322595&dur=328.840&lmt=1713023609357114&mt=1723485655&fvip=3&keepalive=yes&c=IOS&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgcDIwPrpotUxP2GCtUJhy0hhGubkBa-F3XKoUqY0LoiICIB7owsDifMaazFO-cGq1gYdK5i0NiCjbLnM_ENQbIg53&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AGtxev0wRQIgDG4k38xHTqVjVh_93AxTaaHWcXGbddMq2w42oNW7r-ICIQDS9XdVqYOCL8X6Daj4KPPToGOHs5Sj09i08AmRz3Ccxg%3D%3D",
            "ext": "mp4",
            "fileSize": "94.0MB",
            "formatNote": "1080p",
            "hd": true,
            "pro": true,
            "vcodec": "avc1.640028",
            "video": "https://rr1---sn-hp57ynly.googlevideo.com/videoplayback?expire=1723507743&ei=v0-6Zpr1J7CAkucP7rrM4QM&ip=2a05%3A9405%3A0%3A4%3Ad020%3A3%3A0%3A4f50&id=o-ALyHM3FkoX9up_lX2iDj-iUO51kpYwiYtRG7WMPDOIe2&itag=137&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=qr&mm=31%2C29&mn=sn-hp57ynly%2Csn-hp57knds&ms=au%2Crdu&mv=m&mvi=1&pl=32&initcwndbps=741250&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=93267588&dur=328.786&lmt=1713024725770501&mt=1723485655&fvip=3&keepalive=yes&c=IOS&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIhAIIzDVXah5Ksib0iIuQ6jFJCAEcrQaHSqYqGllUMyqV0AiAm19FV5b6gIGe1Q2uJ77NQpv5p-CUxV5ESd0SbYE3nGA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AGtxev0wRQIgDG4k38xHTqVjVh_93AxTaaHWcXGbddMq2w42oNW7r-ICIQDS9XdVqYOCL8X6Daj4KPPToGOHs5Sj09i08AmRz3Ccxg%3D%3D"
        },
        "player": "https://www.amoyshare.com/player/?v=A7ry4cx6HfY&watch=1723486148",
        "publishedAt": "13 years ago",
        "subscribers": "6.3M",
        "thumbnail": "https://i.ytimg.com/vi/A7ry4cx6HfY/mqdefault.jpg",
        "title": "Avenged Sevenfold - So Far Away [Official Music Video]",
        "view_count": "368M"
    },
    "status": 200
}
"""