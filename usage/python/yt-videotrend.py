import requests,json

endpoint = 'https://execross.com/api/v3/ytvideotrend'
headers = {
    'apikey': 'forexecman'
}
params = {
    "region" : "ID",
    "countResult": 15 , # max 25, default 10
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
print(json.dumps(responsed,indent=4))


"""
Result will be:
{
    "creator": "EXECROSS",
    "ip": "182.1.87.23",
    "result": [
        {
            "channelTitle": "beIN SPORTS Indonesia",
            "likeCount": "9340",
            "title": "Manchester City 1-1 Manchester United (pens. 7-6) | FA Community Shield 2024 Match Highlights",
            "url": "https://www.youtube.com/watch?v=9i1SyGF_MLg",
            "videoId": "9i1SyGF_MLg",
            "viewCount": "870652"
        },
        {
            "channelTitle": "Persik Kediri",
            "likeCount": "1700",
            "title": "MATCHDAY 1 - FULL HIGHLIGHTS : PERSIK KEDIRI 1-3 BALI UNITED FC",
            "url": "https://www.youtube.com/watch?v=STTix2kfXk0",
            "videoId": "STTix2kfXk0",
            "viewCount": "183902"
        },
        {
            "channelTitle": "Olympics",
            "likeCount": "33885",
            "title": "THANK YOU PARIS! Closing Ceremony Highlights | #Paris2024",
            "url": "https://www.youtube.com/watch?v=jcB7QA5N7CE",
            "videoId": "jcB7QA5N7CE",
            "viewCount": "2725193"
        },
        {
            "channelTitle": "Persija Jakarta",
            "likeCount": "10144",
            "title": "HIGHLIGHT | Persija 3-0 Barito Putera [BRI Liga 1 2024/2025]",
            "url": "https://www.youtube.com/watch?v=4R9VNJ6lMwo",
            "videoId": "4R9VNJ6lMwo",
            "viewCount": "377435"
        },
        {
            "channelTitle": "Sal Priadi",
            "likeCount": "667451",
            "title": "Sal Priadi - Gala bunga matahari (Official Music Video)",
            "url": "https://www.youtube.com/watch?v=AQpEIZ8dNcU",
            "videoId": "AQpEIZ8dNcU",
            "viewCount": "7612097"
        },
        {
            "channelTitle": "Liverpool FC",
            "likeCount": "36682",
            "title": "HIGHLIGHTS: Luis Diaz double & a Jota screamer! Liverpool 4-1 Sevilla | Pre-Season 2024",
            "url": "https://www.youtube.com/watch?v=y0x_b-Kevls",
            "videoId": "y0x_b-Kevls",
            "viewCount": "1652321"
        },
        {
            "channelTitle": "Hari Jisun",
            "likeCount": "10667",
            "title": "Kasihlah soto ayam + nasi kpd kakak bule yg makan nasi dengan roti\u2026\ud83e\udd23",
            "url": "https://www.youtube.com/watch?v=vihs7dhflRI",
            "videoId": "vihs7dhflRI",
            "viewCount": "204161"
        },
        {
            "channelTitle": "hololive Indonesia",
            "likeCount": "38853",
            "title": "Virtual Medley Lagu Daerah 2024 Ver. - hololive ID [Cover]",
            "url": "https://www.youtube.com/watch?v=rjhIMMSolmc",
            "videoId": "rjhIMMSolmc",
            "viewCount": "219748"
        },
        {
            "channelTitle": "Arsenal",
            "likeCount": "16862",
            "title": "RICCARDO CALAFIORI MAKES DEBUT \u2764\ufe0f | HIGHLIGHTS | Arsenal vs Olympique Lyonnais (2-0) | Emirates Cup",
            "url": "https://www.youtube.com/watch?v=CVmvdGxL1NI",
            "videoId": "CVmvdGxL1NI",
            "viewCount": "808800"
        },
        {
            "channelTitle": "Sie EM",
            "likeCount": "40749",
            "title": "MERANTAU PART 20 - DRAMA ANIMASI",
            "url": "https://www.youtube.com/watch?v=Nvll347uGfc",
            "videoId": "Nvll347uGfc",
            "viewCount": "725345"
        },
        {
            "channelTitle": "Masdddho",
            "likeCount": "30208",
            "title": "BUBAR - MASDDDHO (OFFICIAL MUSIC VIDEO)",
            "url": "https://www.youtube.com/watch?v=ojpe0MBb-GM",
            "videoId": "ojpe0MBb-GM",
            "viewCount": "311878"
        },
        {
            "channelTitle": "PERSIB",
            "likeCount": "15800",
            "title": "TIGA POIN, EMPAT GOL DI LAGA PEMBUKA LIGA \ud83d\udd25 | Highlights PERSIB\u00a04-1\u00a0PSBS\u00a0Biak",
            "url": "https://www.youtube.com/watch?v=SjUV3d-c8UI",
            "videoId": "SjUV3d-c8UI",
            "viewCount": "640756"
        },
        {
            "channelTitle": "MPL Indonesia",
            "likeCount": "5646",
            "title": "RRQ HOSHI vs EVOS GLORY | Regular Season Week 1 Day 2 | Game 1 | #MPLIDS14",       
            "url": "https://www.youtube.com/watch?v=Mny3iORTQeg",
            "videoId": "Mny3iORTQeg",
            "viewCount": "559747"
        },
        {
            "channelTitle": "PSM Makassar",
            "likeCount": "3801",
            "title": "BRI Liga1 - PSM Makassar v Persis Solo 3-0 | Allona PSM",
            "url": "https://www.youtube.com/watch?v=6eqtietwAiE",
            "videoId": "6eqtietwAiE",
            "viewCount": "192558"
        },
        {
            "channelTitle": "TRANS TV Official",
            "likeCount": "23306",
            "title": "Viralnya Hafiz Bersahabat Dengan Seekor Beruk Bernama Bastian | BROWNIS (8/8/24) P1",
            "url": "https://www.youtube.com/watch?v=Ask3qax5DcA",
            "videoId": "Ask3qax5DcA",
            "viewCount": "1961007"
        }
    ],
    "status": 200
}
"""