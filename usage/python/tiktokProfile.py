import requests,json

endpoint = 'https://execross.com/api/v3/tiktok'
headers = {
    'apikey': 'forexecman'
}
params = {
    "userId" : "asking.ang",
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
if responsed['status'] == 200:
    print("Response:",json.dumps(responsed,indent=4))
else:
    print(responsed)

'''
Result will be:

Response: {
    "creator": "EXECROSS",
    "ip": "61.5.71.228",
    "result": {
        "accountId": 2732378204,
        "biography": "",
        "followers": "144",
        "following": "116",
        "location": null,
        "pictureUrl": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/82/76/2c10c080-d113-471b-ac27-8ea331f94b53.jpg",
        "post": [
            {
                "artist": "nemu                            \u2022 \u2022 NEMU GILGA SAHID @RofaRafaNWHD2749",
                "caption": "Nemu sampean \ud83e\udd2d",
                "closed": false,
                "comments": "0",
                "created": "2023-10-17",
                "ensemble": "DUET",
                "gifts": "2",
                "listens": "44",
                "loves": "7",
                "pageUrl": "https://www.smule.com/recording/nemu-nemu-gilga-sahid-rofarafanwhd2749-nemu-gilga-sahid-nemu-nemu-nemu-nemu-nemu-nem/2732403437_4732128989",
                "performances": "1 collab",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-7/sing_google/performance/cover/d7/43/eafe05dd-767a-47c2-a6c3-9e49bb69d5fa.jpg",
                "title": "NEMU GILGA SAHID NEMU NEMU NEMU NEMU NEMU NEM",
                "type": "video"
            },
            {
                "artist": "peterpan",
                "caption": "#allinvited",
                "closed": false,
                "comments": "1",
                "created": "2023-10-14",
                "ensemble": "DUET",
                "gifts": "2",
                "listens": "12",
                "loves": "3",
                "pageUrl": "https://www.smule.com/recording/peterpan-bintang-di-surga-ory/2079376373_4730190483",
                "performances": "GVN_nenkelliss",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/rs-s-sf-2/arr/c3/26/13fc0b7d-c606-4cbb-ae43-478c732962f8.jpg",
                "title": "Bintang di surga ory",
                "type": "audio"
            },
            {
                "artist": "Maulana Ardiansyah",
                "caption": "AC",
                "closed": false,
                "comments": "0",
                "created": "2023-03-01",
                "ensemble": "DUET",
                "gifts": "0",
                "listens": "38",
                "loves": "10",
                "pageUrl": "https://www.smule.com/recording/maulana-ardiansyah-sakit-dalam-bercinta-ska-reggae/2732403437_4584179368",
                "performances": "1 collab",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-5/arr/0d/ce/6fbb0160-7ab4-4b42-9214-e6be6ca40568.jpg",
                "title": "SAKIT DALAM BERCINTA || SKA REGGAE",
                "type": "audio"
            },
            {
                "artist": "Maulana Ardiansyah Ochi Alvira \u2022 Lestari 2 Sigar Nganggur ft",
                "caption": "",
                "closed": false,
                "comments": "0",
                "created": "2023-02-25",
                "ensemble": "SOLO",
                "gifts": "0",
                "listens": "15",
                "loves": "4",
                "pageUrl": "https://www.smule.com/recording/maulana-ardiansyah-ochi-alvira-lestari-2-sigar-nganggur-ft-terlalu-sadis-live-ska-reggae-bl571/2732403437_4581422165",
                "performances": "SusPended404_",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-5/arr/49/9d/0f611681-6679-4783-8e17-0450c36751a3.jpg",
                "title": "TERLALU SADIS [ LIVE SKA REGGAE ] BL571",     
                "type": "audio"
            },
            {
                "artist": "Maulana Ardiansyah",
                "caption": "",
                "closed": false,
                "comments": "0",
                "created": "2023-02-24",
                "ensemble": "SOLO",
                "gifts": "0",
                "listens": "19",
                "loves": "3",
                "pageUrl": "https://www.smule.com/recording/maulana-ardiansyah-sakit-dalam-bercinta-ska-reggae/2732403437_4580914877",
                "performances": "SusPended404_",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-5/arr/0d/ce/6fbb0160-7ab4-4b42-9214-e6be6ca40568.jpg",
                "title": "SAKIT DALAM BERCINTA || SKA REGGAE",
                "type": "audio"
            },
            {
                "artist": "Thomas",
                "caption": "",
                "closed": false,
                "comments": "0",
                "created": "2023-02-24",
                "ensemble": "SOLO",
                "gifts": "0",
                "listens": "10",
                "loves": "0",
                "pageUrl": "https://www.smule.com/recording/thomas-dermaga-biru-versi-2006-dermaga-biru-arya-bl571/2732403437_4580912906",      
                "performances": "SusPended404_",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-7/arr/5d/72/617d28e1-1e9a-467e-94cb-6b0c2413b995.jpg",
                "title": "Dermaga Biru (Versi 2006) - Dermaga Biru Arya BL571",
                "type": "audio"
            },
            {
                "artist": "Maulana Ardiansyah Ft Ochi Alvira _ Luka Sekerat Rasa 2",
                "caption": "Lagi jibek",
                "closed": false,
                "comments": "0",
                "created": "2023-02-22",
                "ensemble": "SOLO",
                "gifts": "0",
                "listens": "23",
                "loves": "0",
                "pageUrl": "https://www.smule.com/recording/maulana-ardiansyah-ft-ochi-alvira-_-luka-sekerat-rasa-2-rela-aku-terima-keputusan-darimu-bl571/2732403437_4579512119",
                "performances": "SusPended404_",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-7/arr/3e/e8/71dd7e05-b942-44d7-a8a3-1eddd1cb1879.jpg",
                "title": "Rela Aku Terima Keputusan Darimu || BL571",   
                "type": "audio"
            },
            {
                "artist": "New Pallapa | Anisa Rahma | GEMANTUNG ROSO | GEMANTUNGE ROSO | KOPLO",
                "caption": "",
                "closed": false,
                "comments": "0",
                "created": "2023-01-25",
                "ensemble": "SOLO",
                "gifts": "0",
                "listens": "21",
                "loves": "4",
                "pageUrl": "https://www.smule.com/recording/new-pallapa-anisa-rahma-gemantung-roso-gemantunge-roso-koplo-gemantunge-roso-koplo-inv/2732403437_4560255270",
                "performances": "SusPended404_",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/rs-s75/arr/d3/67/407aa902-b975-43b6-a8a5-a77ea90d7aa4.jpg",
                "title": "GEMANTUNGE ROSO | KOPLO [INV]",
                "type": "audio"
            },
            {
                "artist": "Original",
                "caption": "#Tak Rela #Musicvideo#salamGVN\ud83e\udd18\ud83d\ude0e",
                "closed": false,
                "comments": "3",
                "created": "2023-01-20",
                "ensemble": "DUET",
                "gifts": "2",
                "listens": "22",
                "loves": "4",
                "pageUrl": "https://www.smule.com/recording/original-tak-rela/2006455888_4556880565",
                "performances": "__nanaaa____",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-6/sing_google/performance/cover/4d/d7/785e0cb8-879c-41f9-af0d-668348ca15c4.jpg",
                "title": "Tak Rela",
                "type": "audio"
            },
            {
                "artist": "Maulana Ardiansyah",
                "caption": "Tiara mana tiara....",
                "closed": false,
                "comments": "2",
                "created": "2023-01-01",
                "ensemble": "DUET",
                "gifts": "0",
                "listens": "59",
                "loves": "15",
                "pageUrl": "https://www.smule.com/recording/maulana-ardiansyah-tiara-ska-reggae-maulana-ardiansyah/2732403437_4543782906",      
                "performances": "3 collabs",
                "private": false,
                "thumbnail": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-7/arr/0e/3e/d0cfb667-105e-44e5-ac1a-b06d01888edb.jpg",
                "title": "TIARA [SKA REGGAE] Maulana Ardiansyah",       
                "type": "audio"
            }
        ],
        "profileUrl": "https://smule.com/SusPended404_",
        "recording": "385",
        "songs": {
            "list": [],
            "next_offset": -1
        },
        "username": "SusPended404_",
        "verified": false,
        "vip": false
    },
    "status": 200
}
'''