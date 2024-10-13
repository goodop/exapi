import requests
import json


url = 'https://execross.com/api/v3/singdl'
headers = {
	"apikey": "forexecman"
}
params = {
	"url":"https://wesingapp.com/user/609c988625283688344f/song/SqImoCqtyzBuvqT8-MalamTerakhir?lang=en&ws_channel=copylink&from_page=2299"
}
datas = requests.get(url,headers=headers,params=params).json()
response = json.dumps(datas,indent=4)
print(response)

'''
{
    "audio": "",
    "avatar": "http://p.kg.qq.com/wsinghead/2153051301/2153051301/100", 
    "comments": [
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2190070842/2190070842/100",
            "content": "kerennn",
            "created": 1720023738,
            "id": "2190070842_1720023738_930206_622",
            "isOwner": 0,
            "nick": "Hasballah Balah",
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609c9485252a3783304c"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2233172484/2233172484/100",
            "content": "ikutan dong",
            "created": 1720278617,
            "id": "2233172484_1720278617_597266_582",
            "isOwner": 0,
            "nick": "Lemin Lemin",
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609f9e86242a358f3c4a"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2223776712/2223776712/100",
            "content": "keren bgt kk cntik",
            "created": 1721197305,
            "id": "2223776712_1721197305_271518_870",
            "isOwner": 0,
            "nick": "\ud835\udc41\ud835\udc89\ud835\udc4e\ud835\udc66", 
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609f9f86222a318c354c"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2178669843/2178669843/100",
            "content": "best OC KK\ud83c\uddee\ud83c\udde9\ud83e\udd73\ud83d\udc4dizin share\ud83d\ude4f",
            "created": 1721269202,
            "id": "2178669843_1721269202_238672_611",
            "isOwner": 0,
            "nick": "\ud83c\udfc1joseph el_wanderer\ud83d\udee0\ufe0f", 
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609c9a8d232b3e83304d"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2157219311/2157219311/100",
            "content": "mantap dek Adinda..",
            "created": 1721831017,
            "id": "2157219311_1721831017_144897_451",
            "isOwner": 0,
            "nick": "Adi putra",
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609c9882272c3e88354f"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2232114205/2232114205/100",
            "content": "keren \ud83d\udc4d\ud83d\udc4d\ud83d\udc4d",    
            "created": 1723029954,
            "id": "2232114205_1723029954_182012_367",
            "isOwner": 0,
            "nick": "\ud834\udd19\u1ddd\ud834\udd19\u0363\ud834\udd19\u036boff",
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609f9e87242c3389344b"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2100773456/2100773456/100",
            "content": "wasyeek,,\ud83d\udc83\ud83d\udc83\ud83d\udc83\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\n,,,, terbaek,,,",
            "created": 1725687123,
            "id": "2100773456_1725687123_749958_400",
            "isOwner": 0,
            "nick": "TS_808",
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609c9d85222a348f3148"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2233846919/2233846919/100",
            "content": "jooosss\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83e\udd70",
            "created": 1725794863,
            "id": "2233846919_1725794863_550731_746",
            "isOwner": 0,
            "nick": "Rider s",
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609f9e862d2931823547"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2234092340/2234092340/100",
            "content": "terbaik",
            "created": 1727174245,
            "id": "2234092340_1727174245_253610_963",
            "isOwner": 0,
            "nick": "\ud83d\udca5\ud83d\udd25Vicky Kra\ud83d\udca5\ud83d\udd25",
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609f9e8125243588304e"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2102351639/2102351639/100",
            "content": "kereeen \u2764\ufe0f\ud83c\udf52\ud83c\udf45\ud83c\udf39\ud83c\udfb8\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d\ud83d\udc4d",
            "created": 1727183451,
            "id": "2102351639_1727183451_324992_668",
            "isOwner": 0,
            "nick": "Tambatan",
            "replyAvatar": "",
            "replyNick": "",
            "uid": "609c9d872628368d3747"
        }
    ],
    "cover": "http://p.kg.qq.com/wsingmvf/600_9dcfbed6b0e9533b706597e683f9fafc59811555/0?j=nMl9ssowtibXicUj8k0ib8575Wlhysouh3Q4mslhx4v2erSwkiaNvTxL4b2eAeG8DBLmWmEoazhBBusAHbsA0WOWFbSD0aB3LL1JPyHj5UPL5iaonROUpdRPklOd4yWaIcvqCY8xicqibHVIUg",
    "created": 1662214899,
    "description": "waiting Paman irama \ud83d\ude0b maaf saltum... \ud83e\udd23\ud83d\ude02",
    "flower": 1212,
    "flowers": [
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2150210328/2150210328/100",
            "nick": "~\ud83d\udee1\ufe0f~Ang man's\ud83c\uddf2\ud83c\udde8",
            "num": 3,
            "type": 0,
            "uid": "609c9885272c37883646"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2179268325/2179268325/100",
            "nick": "HENDRA \ud83c\uddee\ud83c\udde9",
            "num": 1,
            "type": 0,
            "uid": "609c9a8c272b3f88364b"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2218183769/2218183769/100",
            "nick": "Encep Encep",
            "num": 1,
            "type": 0,
            "uid": "609f9c8d2425348c3247"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2121038602/2121038602/100",
            "nick": "Sumantri",
            "num": 1,
            "type": 0,
            "uid": "609c9f84252e3f8d344c"
        },
        {
            "avatar": "http://p.kg.qq.com/wsinghead/2185869736/2185869736/100",
            "nick": "CAPT. CAT SPARROW",
            "num": 1,
            "type": 0,
            "uid": "609c95802d2b3e8c3748"
        }
    ],
    "gift": 9,
    "lyric": null,
    "page": "https://wesingapp.com/user/609c988625283688344f/song/SqImoCqtyzBuvqT8-MalamTerakhir?lang=en&ws_channel=copylink&from_page=2299",   
    "photos": [],
    "play": 11036,
    "rank": 3,
    "score": 2012,
    "singer": "Rhoma Irama(\u7f57\u9a6c\u00b7\u4f0a\u62c9\u9a6c)/Rita Sugiarto(\u4e3d\u5854\u00b7\u82cf\u5409\u4e9a\u6258)",
    "tail": "XiaomiM2007J20CG",
    "title": "Malam Terakhir",
    "type": "video",
    "username": "Adinda Bhadrika",
    "video": "http://wesingapp.stream.kg.qq.com/mv/wesing_cos/83_s_0b2afrk55aab6qalzeyspvrvelaa32eqcksa.f0.mp4?dis_k=81cf647ff2ec435c45a9a464f3bc4d1c&dis_t=1728786706"
}
''' 