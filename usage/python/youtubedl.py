import requests,json

endpoint = 'https://execross.com/api/v3/youtubedl'
headers = {
    'apikey': 'forexecman'
}
params = {
    "url" : "https://youtu.be/_mp547ErQuw?si=wn9Obdk4WaT_c5Qo",  # support all youtube urls included short
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
print(json.dumps(responsed,indent=4))

'''
Result will be:

{
    "creator": "EXECROSS",
    "ip": "182.1.87.23",
    "result": {
        "author": "Bintang Kecil",
        "comments": "0",
        "description": "Dewa 19 - Risalah Hati I Lirik Lagu Indonesia\nDewa 19 - Risalah Hati I Lirik Lagu Indonesia\nDewa 19 - Risalah Hati I Lirik Lagu Indonesia\n\nhttps://youtu.be/_mp547ErQuw\nhttps://youtu.be/_mp547ErQuw\nhttps://youtu.be/_mp547ErQuw\n\nLirik - Risalah Hati\n\nHidupku tanpa cintamu\nBagai malam tanpa bintang\nCintaku tanpa sambutmu\nBagai panas tanpa hujan\n\nJiwaku berbisik lirih\nKu harus milikimu\nAku bisa membuatmu jatuh cinta kepadaku\nMeski kau tak cinta kepadaku\n\nBeri sedikit waktu\nBiar cinta datang karena telah terbiasa\nSimpan mawar yang kuberi\nMungkin wanginya mengilhami\n\nSudikah dirimu untuk\nKenali aku dulu\nSebelum kau ludahi aku\nSebelum kau robek hatiku\n\nAku bisa membuatmu jatuh cinta kepadaku\nBeri sedikit waktu\nBiar cinta datang karena telah terbiasa\nAku bisa membuatmu jatuh cinta kepadaku\n\nMeski kau tak cinta kepadaku\nBeri sedikit waktu\nBiar cinta datang karena telah terbiasa\nAku bisa membuatmu jatuh cinta kepadaku\n\nMeski kau tak cinta kau tak cinta\nAku bisa membuatmu jatuh cinta kepadaku\nMeski kau tak cinta kepadaku\nAku bisa membuatmu jatuh cinta kepadaku\n\nMeski kau tak cinta kepadaku\nBeri sedikit waktu\nBiar cinta datang karena telah terbiasa\nHidupku tanpa cintamu\n\nBagai malam tanpa bintang\nCintaku tanpa sambutmu\nBagai panas tanpa hujan\n\n\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\n#Dewa19 #RisalahHati #LirikLaguIndonesia #VideoLirik #BintangKecil",
        "duration": "04:53",
        "likes": "63",
        "media": {
            "audio": "https://rr2---sn-hp57yns7.googlevideo.com/videoplayback?expire=1723507394&ei=Yk66Zq6BDbuGkucP6ubnoAM&ip=2a05%3A9405%3A0%3A4%3Aca7e%3A3%3A0%3A49ae&id=o-APZw9OeqCx6RG1p83fINcsgyklMAvnP02Rspt0pkK0V3&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=8A&mm=31%2C26&mn=sn-hp57yns7%2Csn-q4fl6nde&ms=au%2Conr&mv=m&mvi=2&pl=32&initcwndbps=186250&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=4738030&dur=292.710&lmt=1723357727633557&mt=1723485418&fvip=4&keepalive=yes&c=IOS&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgX-9so2IkRWdYAxakpScV2KjCO9TnMnhreFURgLTKK4cCIGvweXFXS8S3cstuj_FPHxMFI2hoJHewYQ7MUOvR4mvk&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AGtxev0wRAIgRpQDdLNjnBnMJQFghKDYzgrQjg8eB4Uf72mQUatcLzQCID4XOvoA3FqV-yoYtdajvtfInyPK7ttg68phWObHof90",
            "ext": "mp4",
            "fileSize": "21.0MB",
            "formatNote": "1080p",
            "hd": true,
            "pro": true,
            "vcodec": "avc1.640028",
            "video": "https://rr2---sn-hp57yns7.googlevideo.com/videoplayback?expire=1723507394&ei=Yk66Zq6BDbuGkucP6ubnoAM&ip=2a05%3A9405%3A0%3A4%3Aca7e%3A3%3A0%3A49ae&id=o-APZw9OeqCx6RG1p83fINcsgyklMAvnP02Rspt0pkK0V3&itag=137&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=8A&mm=31%2C26&mn=sn-hp57yns7%2Csn-q4fl6nde&ms=au%2Conr&mv=m&mvi=2&pl=32&initcwndbps=186250&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=17289921&dur=292.640&lmt=1723360106858124&mt=1723485418&fvip=4&keepalive=yes&c=IOS&txp=5535434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgJizHwJJHDaIpwrBDUzl4LuY0_r1zdCJYljjmWiJ92lgCIETOdZYRg5R92JbOxcoF-uOq-MYPL-_KgJFtDhPOs22r&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AGtxev0wRAIgRpQDdLNjnBnMJQFghKDYzgrQjg8eB4Uf72mQUatcLzQCID4XOvoA3FqV-yoYtdajvtfInyPK7ttg68phWObHof90"
        },
        "player": "https://www.amoyshare.com/player/?v=_mp547ErQuw&watch=1723485799",
        "publishedAt": "5 days ago",
        "subscribers": "616",
        "thumbnail": "https://i.ytimg.com/vi/_mp547ErQuw/mqdefault.jpg",
        "title": "Dewa 19 - Risalah Hati I Lirik Lagu Indonesia",
        "view_count": "37K"
    },
    "status": 200
}
'''