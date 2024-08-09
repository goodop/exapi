import requests,json

endpoint = 'https://execross.com/api/v3/smuleprofile'
headers = {
    'apikey': 'forexecman'
}
params = {
    "userId" : "SusPended404_",
    "fullpage": True
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
if responsed['status'] == 200:
    print("Response:",json.dumps(responsed,indent=4))
else:
    print(responsed.content)

'''
Response will be:

Response : {
    "creator": "EXECROSS",
    "ip": "114.125.70.230",
    "result": {
        "profile": {
            "account_id": 2732378204,
            "blurb": "",
            "followees": "116",
            "followers": "146",
            "handle": "SusPended404_",
            "installed_apps": [
                "smuledotcom",
                "sing"
            ],
            "is_current_user_profile": false,
            "is_following": false,
            "is_verified": false,
            "is_vip": false,
            "location": null,
            "num_performances": "385",
            "pic_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/82/76/2c10c080-d113-471b-ac27-8ea331f94b53.jpg",        
            "sfam_count": 0,
            "url": "/SusPended404_",
            "verified_type": "unverified",
            "wallet": null
        }
    },
    "status": 200
}

Full Page:

Response: {
    "creator": "EXECROSS",
    "ip": "114.125.70.230",
    "result": {
        "performance": {
            "list": [
                {
                    "app_uid": "sing_google",
                    "arr_key": "18973975_18973975",
                    "arr_type": null,
                    "artist": "nemu                            \u2022 \u2022 NEMU GILGA SAHID @RofaRafaNWHD2749",
                    "artist_twitter": null,
                    "child_count": 1,
                    "closed": false,
                    "cover_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-7/sing_google/performance/cover/d7/43/eafe05dd-767a-47c2-a6c3-9e49bb69d5fa.jpg",
                    "created_at": "2023-10-17T07:18:23.000Z",
                    "duet": null,
                    "ensemble_type": "DUET",
                    "expire_at": "2023-10-24T07:18:23.000Z",
                    "featured": false,
                    "form_type": "full",
                    "join_link": null,
                    "key": "2732403437_4732128989",
                    "media_url": "e:p4MNZY0bvW4P7TxXdrhhMv0IIEwv+Vz5g5i0YyNusjKlEjNtatH9uSUmQYZZutlwX0+CArK4jMyhudFFhc6xSi3ADbJParYR7ofwghNbq9IvpWxkTNrKR08Eu5ate4kYn3MmaAU+afo2RSRWAyCZXuaEhOpg5Ix9TRCG9A==",    
                    "message": "Nemu sampean \ud83e\udd2d",
                    "other": null,
                    "other_performers": [],
                    "owner": {
                        "account_id": 2732378204,
                        "discount": 114.2,
                        "handle": "SusPended404_",
                        "is_verified": false,
                        "is_vip": false,
                        "pic_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/82/76/2c10c080-d113-471b-ac27-8ea331f94b53.jpg",
                        "price": 22.4,
                        "url": "/SusPended404_",
                        "verified_type": "unverified"
                    },
                    "perf_status": "e",
                    "performance_key": "2732403437_4732128989",       
                    "performed_by": "1 collab",
                    "performed_by_url": "/SusPended404_",
                    "poi": null,
                    "private": false,
                    "rec_id": null,
                    "rm": null,
                    "seed": true,
                    "segments": null,
                    "song_info_url": null,
                    "song_length": null,
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
                    "title": "NEMU GILGA SAHID NEMU NEMU NEMU NEMU NEMU NEM",
                    "type": "video",
                    "video_media_mp4_url": "e:p4MNZY0bvW4P7TxXdrhhMv0IIEwv+Vz5g5i0YyNusjKlEjNtatH9uSUmQYZZutlwX0+CArK4jMyhudFFhc6xSi3ADbJParYR/Ivmghhbq4Qv9DtkHYifExtU7sCtKIUTz3MmOFJvaaFnTXJWAimcA7DYgus0t9l1TRDCoQ==",
                    "video_media_url": "e:p4MNZY0bvW4P7TxXdrhhMv0IIEwv+Vz5g5i0YyNusjKlEjNtatH9uSUmQYZZutlwX0+CArK4jMyhudFFhc6xSi3ADbJParYR/Ivmghhbq4Qv9DtkHYifExtU7sCtKIUTz3MmOFJvaaFnTXJWAimcA7DYgus0t9l1TRDCoQ==",
                    "video_resolution": "360x360",
                    "visualizer_media_url": null,
                    "web_url": "/recording/nemu-nemu-gilga-sahid-rofarafanwhd2749-nemu-gilga-sahid-nemu-nemu-nemu-nemu-nemu-nem/2732403437_4732128989"
                },
                {
                    "app_uid": "sing_google",
                    "arr_key": "14487650_14487650",
                    "arr_type": null,
                    "artist": "peterpan",
                    "artist_twitter": null,
                    "child_count": 0,
                    "closed": false,
                    "cover_url": "https://c-fa.cdn.smule.com/rs-s-sf-2/arr/c3/26/13fc0b7d-c606-4cbb-ae43-478c732962f8.jpg",
                    "created_at": "2023-10-14T09:34:43.000Z",
                    "duet": {
                        "account_id": 2732378204,
                        "handle": "SusPended404_",
                        "is_verified": false,
                        "is_vip": false,
                        "pic_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/82/76/2c10c080-d113-471b-ac27-8ea331f94b53.jpg",
                        "url": "/SusPended404_",
                        "verified_type": "unverified"
                    },
                    "ensemble_type": "DUET",
                    "expire_at": null,
                    "featured": false,
                    "form_type": "full",
                    "join_link": null,
                    "key": "2079376373_4730190483",
                    "media_url": "e:p4MNZY0bvW4P7TxXdrhhMv0IIEwv+Vz5g5i0YyNusjKlEjNtatH9uSV7WpgFoN55Z3eKArqzhYb+rMZRjNOuRiLNC/gSfb0b75Dng1gS+Zgyp3F8SNiRQh9fvNq4eIgZ1momPgAmfKY2FWhIA3XPA+CO0O5m4IlrDknT",        
                    "message": "#allinvited",
                    "other": {
                        "id": 2732378204,
                        "label": "SusPended404_",
                        "pic_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/82/76/2c10c080-d113-471b-ac27-8ea331f94b53.jpg",
                        "url": "/SusPended404_",
                        "verified_type": "unverified",
                        "vip": false
                    },
                    "other_performers": [
                        {
                            "account_id": 2732378204,
                            "handle": "SusPended404_",
                            "is_verified": false,
                            "is_vip": false,
                            "pic_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/82/76/2c10c080-d113-471b-ac27-8ea331f94b53.jpg",
                            "url": "/SusPended404_",
                            "verified_type": "unverified"
                        }
                    ],
                    "owner": {
                        "account_id": 2079371282,
                        "discount": 118.4,
                        "handle": "GVN_nenkelliss",
                        "is_verified": false,
                        "is_vip": true,
                        "pic_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/da/69/de9b67a9-7865-4528-934c-a5d33d38cab1.jpg",
                        "price": 24.4,
                        "url": "/GVN_nenkelliss",
                        "verified_type": "unverified"
                    },
                    "perf_status": "n",
                    "performance_key": "2079376373_4730190483",       
                    "performed_by": "GVN_nenkelliss",
                    "performed_by_url": "/GVN_nenkelliss",
                    "poi": null,
                    "private": false,
                    "rec_id": null,
                    "rm": null,
                    "seed": false,
                    "segments": null,
                    "song_info_url": null,
                    "song_length": null,
                    "stats": {
                        "total_commenters": 0,
                        "total_comments": 1,
                        "total_gifts": 2,
                        "total_listens": 12,
                        "total_loves": 3,
                        "total_performers": 2,
                        "truncated_comments": "1",
                        "truncated_gifts": "2",
                        "truncated_listens": "12",
                        "truncated_loves": "3",
                        "truncated_other_performers": "1"
                    },
                    "title": "Bintang di surga ory",
                    "type": "audio",
                    "video_media_mp4_url": null,
                    "video_media_url": null,
                    "visualizer_media_url": null,
                    "web_url": "/recording/peterpan-bintang-di-surga-ory/2079376373_4730190483"
                },
                {
                    "app_uid": "sing_google",
                    "arr_key": "17303413_17303413",
                    "arr_type": null,
                    "artist": "Maulana Ardiansyah",
                    "artist_twitter": null,
                    "child_count": 1,
                    "closed": false,
                    "cover_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-s-5/arr/0d/ce/6fbb0160-7ab4-4b42-9214-e6be6ca40568.jpg",
                    "created_at": "2023-03-01T02:29:44.000Z",
                    "duet": null,
                    "ensemble_type": "DUET",
                    "expire_at": "2023-03-08T02:29:44.000Z",
                    "featured": false,
                    "form_type": "full",
                    "join_link": null,
                    "key": "2732403437_4584179368",
                    "media_url": "e:p4MNZY0bvW4P7TxXdrhhMv0IIEwv+Vz5g5i0YyNusjKlEjNtatH9uSV7WpgFoN55Z3eKArqzhYb+rMZRjNOuRiLNC/gSfb0b75Dng1gR/pg0p3EtRtzLE0leudriKIcT1mpwbAImJfBgQGhIAXTKALWE0LgysIlrDknT",        
                    "message": "AC",
                    "other": null,
                    "other_performers": [],
                    "owner": {
                        "account_id": 2732378204,
                        "discount": -122.4,
                        "handle": "SusPended404_",
                        "is_verified": false,
                        "is_vip": false,
                        "pic_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/82/76/2c10c080-d113-471b-ac27-8ea331f94b53.jpg",
                        "price": 37.8,
                        "url": "/SusPended404_",
                        "verified_type": "unverified"
                    },
                    "perf_status": "e",
                    "performance_key": "2732403437_4584179368",       
                    "performed_by": "1 collab",
                    "performed_by_url": "/SusPended404_",
                    "poi": null,
                    "private": false,
                    "rec_id": null,
                    "rm": null,
                    "seed": true,
                    "segments": null,
                    "song_info_url": null,
                    "song_length": null,
                    "stats": {
                        "total_commenters": 0,
                        "total_comments": 0,
                        "total_gifts": 0,
                        "total_listens": 38,
                        "total_loves": 10,
                        "total_performers": 1,
                        "truncated_comments": "0",
                        "truncated_gifts": "0",
                        "truncated_listens": "38",
                        "truncated_loves": "10",
                        "truncated_other_performers": "0"
                    },
                    "title": "SAKIT DALAM BERCINTA || SKA REGGAE",    
                    "type": "audio",
                    "video_media_mp4_url": null,
                    "video_media_url": null,
                    "visualizer_media_url": null,
                    "web_url": "/recording/maulana-ardiansyah-sakit-dalam-bercinta-ska-reggae/2732403437_4584179368"
                }
            ],
            "next_offset": 3
        },
        "profile": {
            "account_id": 2732378204,
            "blurb": "",
            "followees": "116",
            "followers": "146",
            "handle": "SusPended404_",
            "installed_apps": [
                "sing",
                "smuledotcom"
            ],
            "is_current_user_profile": false,
            "is_following": false,
            "is_verified": false,
            "is_vip": false,
            "location": null,
            "num_performances": "385",
            "pic_url": "https://c-fa.cdn.smule.com/smule-gg-uw1-z-1/account/picture/82/76/2c10c080-d113-471b-ac27-8ea331f94b53.jpg",        
            "sfam_count": 0,
            "url": "/SusPended404_",
            "verified_type": "unverified",
            "wallet": null
        },
        "songs": {
            "list": [],
            "next_offset": -1
        }
    },
    "status": 200
}

'''