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
    "ip": "125.164.15.3",
    "result": [
        {
            "channelTitle": "Sal Priadi",
            "likeCount": "675796",
            "title": "Sal Priadi - Gala bunga matahari (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=AQpEIZ8dNcU",
            "videoId": "AQpEIZ8dNcU",
            "viewCount": "7857796"
        },
        {
            "channelTitle": "Fauzana Official",
            "likeCount": "131715",
            "title": "Fauzana - Ciinan Bana (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=Pj4zgZLzRlM",
            "videoId": "Pj4zgZLzRlM",
            "viewCount": "3256912"
        },
        {
            "channelTitle": "Yovie Widianto",
            "likeCount": "123835",
            "title": "Yovie Widianto, Lyodra - Terlalu Cinta (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=oZ2cUnrFyoA",
            "videoId": "oZ2cUnrFyoA",
            "viewCount": "5794708"
        },
        {
            "channelTitle": "Henny Adella",
            "likeCount": "9350",
            "title": "SALAHMU SENDIRI - Difarina Indra Adella Ft. Fendik Adella - OM ADELLA",  
            "url": "https://www.youtube.com/watch?v=2udLd3_0nGk",
            "videoId": "2udLd3_0nGk",
            "viewCount": "751373"
        },
        {
            "channelTitle": "Salma Salsabil",
            "likeCount": "52795",
            "title": "Salma Salsabil - affa iyah feat. Basboi (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=HSTO6FPSIj0",
            "videoId": "HSTO6FPSIj0",
            "viewCount": "525350"
        },
        {
            "channelTitle": "Masdddho",
            "likeCount": "30686",
            "title": "BUBAR - MASDDDHO (OFFICIAL MUSIC VIDEO)",
            "url": "https://www.youtube.com/watch?v=ojpe0MBb-GM",
            "videoId": "ojpe0MBb-GM",
            "viewCount": "323199"
        },
        {
            "channelTitle": "MAHESA Official",
            "likeCount": "11665",
            "title": "GERRY MAHESA FT DINDA TERATU - PUPUSING NELONGSO I Mahesa Music",        
            "url": "https://www.youtube.com/watch?v=jb6wmnnykJI",
            "videoId": "jb6wmnnykJI",
            "viewCount": "547014"
        },
        {
            "channelTitle": "YURA YUNITA",
            "likeCount": "35150",
            "title": "Yura Yunita - Risalah Hati (Live From Pertunjukan Tutur Batin Jakarta)", 
            "url": "https://www.youtube.com/watch?v=rtaS84m4USE",
            "videoId": "rtaS84m4USE",
            "viewCount": "1305829"
        },
        {
            "channelTitle": "RC Music",
            "likeCount": "8492",
            "title": "SILVY KUMALASARI - PUJANINGSIH ( Official Live Video Royal Music )",     
            "url": "https://www.youtube.com/watch?v=P-P7NVn4vbQ",
            "videoId": "P-P7NVn4vbQ",
            "viewCount": "556281"
        },
        {
            "channelTitle": "Koplo Time",
            "likeCount": "4217",
            "title": "Awal mulanya ditertawakan endingnya malah dapat hadiah dari pengunjung", 
            "url": "https://www.youtube.com/watch?v=B_FUnSmkqT0",
            "videoId": "B_FUnSmkqT0",
            "viewCount": "246500"
        }
    ],
    "status": 200
}

"""