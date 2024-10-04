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
    "ip": "61.5.71.228",
    "result": {
        "audioUrl": "https://rr1---sn-capm-vnae.googlevideo.com/videoplayback?expire=1728046476&ei=LJH_ZpCSJPaI6dsPyOCwyAY&ip=172.84.183.150&id=o-AHKr4k5GdtWWgwxshrY5PRf2em238IGFgASWjZ0_-2dU&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=8A&mm=31%2C29&mn=sn-capm-vnae%2Csn-5hne6nsk&ms=au%2Crdu&mv=m&mvi=1&pl=24&initcwndbps=1182500&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=4738030&dur=292.710&lmt=1723357727633557&mt=1728024540&fvip=3&keepalive=yes&fexp=51300761&c=IOS&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIgXc_6vrL0ID54yBZzZCrhv_LYm1633LLVoJYZYu1zkSwCIQCaf8tlQ9PoE1YijzaB9HHc7DNwoyb0WpzAlzs4kAWGGA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ACJ0pHgwRQIhALWkaDmB-5sgpHN_3xY8NnqaGjBoyEpzHyblOI1cAEBgAiBFrxQgcQOFIsA5-zv7sgRQGbzaC11xf2esLqHOug0yHw%3D%3D",
        "author": "Bintang Kecil",
        "comments": "5",
        "description": "Dewa 19 - Risalah Hati I Lirik Lagu Indonesia\nDewa 19 - Risalah Hati I Lirik Lagu Indonesia\nDewa 19 - Risalah Hati I Lirik Lagu Indonesia\n\nhttps://youtu.be/_mp547ErQuw\nhttps://youtu.be/_mp547ErQuw\nhttps://youtu.be/_mp547ErQuw\n\nLirik - Risalah Hati\n\nHidupku tanpa cintamu\nBagai malam tanpa bintang\nCintaku tanpa sambutmu\nBagai panas tanpa hujan\n\nJiwaku berbisik lirih\nKu harus milikimu\nAku bisa membuatmu jatuh cinta kepadaku\nMeski kau tak cinta kepadaku\n\nBeri sedikit waktu\nBiar cinta datang karena telah terbiasa\nSimpan mawar yang kuberi\nMungkin wanginya mengilhami\n\nSudikah dirimu untuk\nKenali aku dulu\nSebelum kau ludahi aku\nSebelum kau robek hatiku\n\nAku bisa membuatmu jatuh cinta kepadaku\nBeri sedikit waktu\nBiar cinta datang karena telah terbiasa\nAku bisa membuatmu jatuh cinta kepadaku\n\nMeski kau tak cinta kepadaku\nBeri sedikit waktu\nBiar cinta datang karena telah terbiasa\nAku bisa membuatmu jatuh cinta kepadaku\n\nMeski kau tak cinta kau tak cinta\nAku bisa membuatmu jatuh cinta kepadaku\nMeski kau tak cinta kepadaku\nAku bisa membuatmu jatuh cinta kepadaku\n\nMeski kau tak cinta kepadaku\nBeri sedikit waktu\nBiar cinta datang karena telah terbiasa\nHidupku tanpa cintamu\n\nBagai malam tanpa bintang\nCintaku tanpa sambutmu\nBagai panas tanpa hujan\n\n\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\n#Dewa19 #RisalahHati #LirikLaguIndonesia #VideoLirik #BintangKecil",
        "duration": "04:53",
        "format": "1080p",
        "likes": "",
        "pageUrl": "https://www.youtube.com/watch?v=_mp547ErQuw",       
        "player": "https://www.amoyshare.com/player/?v=_mp547ErQuw&watch=1728024884",
        "publishedAt": "1 month ago",
        "size": "21.0MB",
        "subscribers": "2.13K",
        "thumbnail": "https://i.ytimg.com/vi/_mp547ErQuw/mqdefault.jpg",
        "title": "Dewa 19 - Risalah Hati I Lirik Lagu Indonesia",       
        "videoUrl": "https://rr1---sn-capm-vnae.googlevideo.com/videoplayback?expire=1728046477&ei=LZH_ZtmrN6yO6dsPub3quAI&ip=172.84.183.150&id=o-AOO27XMainKv1Bk7O69bMdynxxLJORRqUikHsaq1khy_&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=8A&mm=31%2C29&mn=sn-capm-vnae%2Csn-5hnekn7s&ms=au%2Crdu&mv=m&mvi=1&pl=24&initcwndbps=1182500&bui=AXLXGFQKEj4oHjq7V8L_9fwCZwS6SdG_nCUBj-vWanPka2Zw25TfZQ-2jiy6xT7skcJKa2F_F3CJGq9m&spc=54MbxbPxr1X1uDUDpTn0X01_Es7Vn5303rOskySp5GgcThu3Xs_p&vprv=1&svpuc=1&mime=video%2Fmp4&ns=4GnGoqDVJndGD8NH10083oMQ&rqh=1&gir=yes&clen=6403914&ratebypass=yes&dur=292.710&lmt=1723359381565994&mt=1728024540&fvip=2&fexp=51300761&c=WEB_CREATOR&sefc=1&txp=5538434&n=bb-6DpJwE2Nz2w&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ACJ0pHgwRQIgBl2bWoUguaGQS6gUVJVhy6MZPdtF2ZdsPDU0mWHgSgkCIQD3CEKQdRXdhJIh4CFMkjd8FxUpL9LGAT-S5WAiA78BpQ%3D%3D&sig=AJfQdSswRQIgSdMY7inD5-_PTBBnWB7iasmGdMtf8EYUPcf5WP3KGMECIQD_NgOkwiPyLM4xhNEKh6kaIl70jxzgwW9kY0pR8TExOA%3D%3D",
        "watched": "121K"
    },
    "status": 200
}
'''