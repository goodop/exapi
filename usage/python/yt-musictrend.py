import requests,json

endpoint = 'https://execross.com/api/v3/ytmusictrend'
headers = {
    'apikey': 'forexecman'
}
params = {
    "region" : "ID",
    "countResult": 10 , # max 30, default 10
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
print(json.dumps(responsed,indent=4))

"""
Return will be:
{
    "creator": "EXECROSS",
    "ip": "182.1.91.138",
    "result": [
        {
            "channelTitle": "Sal Priadi",
            "likeCount": "715901",
            "thumbnailUrl": "https://i.ytimg.com/vi/AQpEIZ8dNcU/hqdefault.jpg",
            "title": "Sal Priadi - Gala bunga matahari (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=AQpEIZ8dNcU",
            "videoId": "AQpEIZ8dNcU",
            "viewCount": "9397027"
        },
        {
            "channelTitle": "Fauzana Official",
            "likeCount": "136159",
            "thumbnailUrl": "https://i.ytimg.com/vi/Pj4zgZLzRlM/hqdefault.jpg",
            "title": "Fauzana - Ciinan Bana (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=Pj4zgZLzRlM",
            "videoId": "Pj4zgZLzRlM",
            "viewCount": "3555436"
        },
        {
            "channelTitle": "Henny Adella",
            "likeCount": "9914",
            "thumbnailUrl": "https://i.ytimg.com/vi/2udLd3_0nGk/hqdefault.jpg",
            "title": "SALAHMU SENDIRI - Difarina Indra Adella Ft. Fendik Adella - OM ADELLA",
            "url": "https://www.youtube.com/watch?v=2udLd3_0nGk",
            "videoId": "2udLd3_0nGk",
            "viewCount": "841740"
        },
        {
            "channelTitle": "Yovie Widianto",
            "likeCount": "125254",
            "thumbnailUrl": "https://i.ytimg.com/vi/oZ2cUnrFyoA/hqdefault.jpg",
            "title": "Yovie Widianto, Lyodra - Terlalu Cinta (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=oZ2cUnrFyoA",
            "videoId": "oZ2cUnrFyoA",
            "viewCount": "6111589"
        },
        {
            "channelTitle": "Salma Salsabil",
            "likeCount": "53999",
            "thumbnailUrl": "https://i.ytimg.com/vi/HSTO6FPSIj0/hqdefault.jpg",
            "title": "Salma Salsabil - affa iyah feat. Basboi (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=HSTO6FPSIj0",
            "videoId": "HSTO6FPSIj0",
            "viewCount": "579752"
        },
        {
            "channelTitle": "Koplo Time",
            "likeCount": "5105",
            "thumbnailUrl": "https://i.ytimg.com/vi/B_FUnSmkqT0/hqdefault.jpg",
            "title": "Awal mulanya ditertawakan endingnya malah dapat hadiah dari pengunjung",
            "url": "https://www.youtube.com/watch?v=B_FUnSmkqT0",
            "videoId": "B_FUnSmkqT0",
            "viewCount": "340394"
        },
        {
            "channelTitle": "Masdddho",
            "likeCount": "32356",
            "thumbnailUrl": "https://i.ytimg.com/vi/ojpe0MBb-GM/hqdefault.jpg",
            "title": "BUBAR - MASDDDHO (OFFICIAL MUSIC VIDEO)",
            "url": "https://www.youtube.com/watch?v=ojpe0MBb-GM",
            "videoId": "ojpe0MBb-GM",
            "viewCount": "370658"
        },
        {
            "channelTitle": "MAHESA Official",
            "likeCount": "12399",
            "thumbnailUrl": "https://i.ytimg.com/vi/jb6wmnnykJI/hqdefault.jpg",
            "title": "GERRY MAHESA FT DINDA TERATU - PUPUSING NELONGSO I Mahesa Music",
            "url": "https://www.youtube.com/watch?v=jb6wmnnykJI",
            "videoId": "jb6wmnnykJI",
            "viewCount": "611820"
        },
        {
            "channelTitle": "Berkah Talenta",
            "likeCount": "2979",
            "thumbnailUrl": "https://i.ytimg.com/vi/lf-rgIsx92A/hqdefault.jpg",
            "title": "Shinta Arsinta Feat Arya Galih - Kawin Kontrak (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=lf-rgIsx92A",
            "videoId": "lf-rgIsx92A",
            "viewCount": "303029"
        },
        {
            "channelTitle": "RC Music",
            "likeCount": "9345",
            "thumbnailUrl": "https://i.ytimg.com/vi/P-P7NVn4vbQ/hqdefault.jpg",
            "title": "SILVY KUMALASARI - PUJANINGSIH ( Official Live Video Royal Music )",
            "url": "https://www.youtube.com/watch?v=P-P7NVn4vbQ",
            "videoId": "P-P7NVn4vbQ",
            "viewCount": "660077"
        }
    ],
    "status": 200
}
"""