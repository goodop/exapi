import requests,json

endpoint = 'https://execross.com/api/v3/smuledl'
headers = {
    'apikey': 'forexecman'
}
params = {
    "url" : "https://www.smule.com/sing-recording/2732403437_4732128989",
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
if responsed['status'] == 200:
    print("Response:",json.dumps(responsed,indent=4))
else:
    print(responsed.content)

''' Response Will be:

Response: {
    "creator": "EXECROSS",
    "ip": "114.125.70.230",
    "result": {
        "artist": "nemu                            \u2022 \u2022 NEMU GILGA SAHID @RofaRafaNWHD2749",
        "audio": "https://c-fa.cdn.smule.com/smule-gg-uw1-rp-1/sing_google/performance/rendered/7e/c2/23ba6cca-b83d-4465-941a-21f8b82bc2d8.m4a",
        "created": "2023-10-17T00:18:23-07:00",
        "detail": true,
        "ensemble": "DUET",
        "expired": "2023-10-24T00:18:23-07:00",
        "message": "Nemu sampean \ud83e\udd2d",
        "owner": {
            "account_id": 2732378204,
            "discount": 114.2,
            "handle": "SusPended404_",
            "is_verified": false,
            "is_vip": false,
            "pic_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/82/76/2c10c080-d113-471b-ac27-8ea331f94b53.jpg",        
            "price": 22.5,
            "url": "/SusPended404_",
            "verified_type": "unverified"
        },
        "stats": {
            "total_commenters": 0,
            "total_comments": 0,
            "total_gifts": 2,
            "total_listens": 43,
            "total_loves": 7,
            "total_performers": 1,
            "truncated_comments": "0",
            "truncated_gifts": "2",
            "truncated_listens": "43",
            "truncated_loves": "7",
            "truncated_other_performers": "0"
        },
        "thumbnail": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-7/sing_google/performance/cover/d7/43/eafe05dd-767a-47c2-a6c3-9e49bb69d5fa.jpg",
        "title": "NEMU GILGA SAHID NEMU NEMU NEMU NEMU NEMU NEM",     
        "type": "video",
        "video": "https://c-fa.cdn.smule.com/smule-gg-uw1-rp-1/sing_google/performance/renvideo/73/2e/ca75b367-1484-4dad-be97-38ce4d4c7a10.mp4"
    },
    "status": 200
}

'''