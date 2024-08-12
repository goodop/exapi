import requests,json

endpoint = 'https://execross.com/api/v3/instastory'
headers = {
    'apikey': 'forexecman'
}
params = {
    "userid" : "anyageraldine",
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
if responsed['status'] == 200:
    print("Response:",json.dumps(responsed,indent=4))
else:
    print(responsed)


'''
Response will be:
Response: {
    "creator": "EXECROSS",
    "ip": "182.1.80.151",
    "result": {
        "data": {
            "image": [
                {
                    "height": 2282,
                    "url": "https://scontent-cdg4-3.cdninstagram.com/v/t51.29350-15/454850568_1018329586667059_3339430689413445897_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMjg0eDIyODIuc2RyLmYyOTM1MCJ9&_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=1&_nc_ohc=R_VOgjBeqQ8Q7kNvgF54T2O&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=MzQzMjA5MTg1OTQ0OTg2OTA1Ng%3D%3D.2-ccb7-5&oh=00_AYB7FW5TevTHhuvkOuFDbTu8tPJYhgalzoXdeV0fZENSsw&oe=66BED13B&_nc_sid=982cc7",
                    "url_signature": {
                        "expires": 1723404367,
                        "signature": "Y5NTLW66-PHpE8asV5HHMA"
                    },
                    "width": 1284
                },
                {
                    "height": 2282,
                    "url": "https://scontent-cdg4-1.cdninstagram.com/v/t51.29350-15/455081628_1200313901293877_6124566969559451825_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMjg0eDIyODIuc2RyLmYyOTM1MCJ9&_nc_ht=scontent-cdg4-1.cdninstagram.com&_nc_cat=105&_nc_ohc=oIeB4CLFREcQ7kNvgErVbBE&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=MzQzMjM4MzA1OTE2MzczODA0NA%3D%3D.2-ccb7-5&oh=00_AYDrRFUytu7H_tOLbnBmK6Z_G-kVoLpDXmwyPjqov4SG8g&oe=66BED7AD&_nc_sid=982cc7",
                    "url_signature": {
                        "expires": 1723404367,
                        "signature": "rwJw-Aez0eVLUM3bJLHZwA"
                    },
                    "width": 1284
                },
                {
                    "height": 2282,
                    "url": "https://scontent-cdg4-3.cdninstagram.com/v/t51.29350-15/454897997_485662424277066_3306895361730856888_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMjg0eDIyODIuc2RyLmYyOTM1MCJ9&_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=106&_nc_ohc=5upSeOWNe04Q7kNvgEMZ21O&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=MzQzMjM4NDYxNTQ1MTc2NDgwNA%3D%3D.2-ccb7-5&oh=00_AYDUTU47LpfbtcSkjq-eQ26AYSJqIz5AxT9WFu5OL1Nrgg&oe=66BEC980&_nc_sid=982cc7",
                    "url_signature": {
                        "expires": 1723404367,
                        "signature": "pvRn18o0JT2ecH94bUb8pw"
                    },
                    "width": 1284
                }
            ],
            "video": [
                {
                    "height": 1920,
                    "type": 101,
                    "url": "https://scontent.cdninstagram.com/o1/v/t16/f2/m69/An97RteVjKPfG6dSLQ_-_fxjlExMxiEVM7aecsI2_HTMdJBCPBJNr5jz5nOHmF90QLuD3679ZR14fvn6KJmteetv.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzIuMTA4MC5kYXNoX2Jhc2VsaW5lXzEwODBwX3YxIn0&_nc_ht=scontent.cdninstagram.com&_nc_cat=104&strext=1&vs=5dae1e876498df40&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTlM1UFFOLXZKSUFYRzRCQU5XREtyQy1rNmRFYnBSMUFBQUYVAALIAQAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACau88mi6%2BDvARUCKAJDMiwXQBgAAAAAAAAYFmRhc2hfYmFzZWxpbmVfMTA4MHBfdjERAHXoBwA%3D&ccb=9-4&oh=00_AYBnBvgs1notKdU80lrrJj95lFZx4Grx7BMZ2ln3m9MjQQ&oe=66BAE8A6&_nc_sid=1d576d",
                    "url_signature": {
                        "expires": 1723404367,
                        "signature": "MNSMDm-pj29QFEBGvcwupw"
                    },
                    "width": 1080
                },
                {
                    "height": 1280,
                    "type": 101,
                    "url": "https://scontent.cdninstagram.com/o1/v/t16/f1/m78/F842A17D3521B19FE71882AEDE12479F_video_dashinit.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzIuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSJ9&_nc_ht=scontent.cdninstagram.com&_nc_cat=105&vs=964f123cd0d04d59&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0Y4NDJBMTdEMzUyMUIxOUZFNzE4ODJBRURFMTI0NzlGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBABUCGDpwYXNzdGhyb3VnaF9ldmVyc3RvcmUvR0R4LXJBSkprV1dSTU5FQkFJZTRDNER1bVN3aWJwUjFBQUFGFQICyAEAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmmOaWpeHHlw4VAigCQzIsF0AUzMzMzMzNGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoBwA%3D&ccb=9-4&oh=00_AYD834IzGzc_ZXAn2YF8PecxBfZwgpcIaRYOwx2z2PTn3A&oe=66BACD4A&_nc_sid=1d576d",
                    "url_signature": {
                        "expires": 1723404367,
                        "signature": "ZG2SEO9ivsWm_a1A7aIWqA"
                    },
                    "width": 720
                }
            ]
        }
    },
    "status": 200
}
'''