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
        "biography": "https://ang.execross.pw",
        "digg": 0,
        "followers": 503,
        "following": 4,
        "ftc": false,
        "fullname": "asking.ang",
        "lastpost": [
            {
                "comment": 0,
                "created": 1705989277,
                "desc": "",
                "download": 3,
                "like": 0,
                "pageUrl": "https://www.tiktok.com/@asking.ang/video/oYySIvYCABiG7oFyzVlAfiK3ogkbBE8KI61WdJ",
                "playing": 3,
                "poster": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/ocvoEkzKBBAJV8xxX6i3gIyA2C7oYAb1IWfQvi~tplv-tiktokx-cropcenter-q:300:400:q72.jpeg?dr=14782&nonce=64936&refresh_token=809ed2e841b246cfff7898be79735acd&x-expires=1728129600&x-signature=iIDqiLdtwJpM7cD9u6RbOIpCIFY%3D&biz_tag=tt_video&idc=maliva&ps=933b5bde&s=PUBLISH&sc=cover&shcp=132edbea&shp=d05b14bd&t=bacd0480",
                "share": 0,
                "videoUrl": "https://v16m.tiktokcdn.com/89acee3d26afe5512e788074da98501a/6700305b/video/tos/useast2a/tos-useast2a-pve-0068/oYySIvYCABiG7oFyzVlAfiK3ogkbBE8KI61WdJ/?a=1233&bti=M0BzMzU8OGYpNzo5Zi5wIzEuLjpkNDQwOg%3D%3D&ch=0&cr=13&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C&br=892&bt=446&cs=0&ds=6&ft=rO54i0z112NJYOcyUNxRNPvE86~O_5ByXsnzXtG&mime_type=video_mp4&qs=0&rc=ZDQ1NzU1ODM6OWk4Zzg8OkBpanJ1aXE5cjNvcDMzNzczM0A1NTNfMDIyNjIxNDRhNV4zYSNtai8yMmRzNWtgLS1kMTZzcw%3D%3D&vvpl=1&l=20241004121335117415D78073888893A4&btag=e00088000&cc=3"
            },
            {
                "comment": 0,
                "created": 1705988175,
                "desc": "",
                "download": 2,
                "like": 0,
                "pageUrl": "https://www.tiktok.com/@asking.ang/video/oAEDlrQ8TnA1EBUfPMBBD8PAE2JFvQBISQfFRU",
                "playing": 2,
                "poster": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/ogflg8RSESDrnvCE0UFBAEsEBUQSIQB81QAJfA~tplv-tiktokx-cropcenter-q:300:400:q72.jpeg?dr=14782&nonce=28406&refresh_token=3eff0e039ebc999c3a1524742d1897f3&x-expires=1728129600&x-signature=V3LBpZ7lUFgD6hrUwKmXWoHqPhE%3D&biz_tag=tt_video&idc=maliva&ps=933b5bde&s=PUBLISH&sc=cover&shcp=132edbea&shp=d05b14bd&t=bacd0480",
                "share": 0,
                "videoUrl": "https://v16m.tiktokcdn.com/dfc58a91a7468ef5439bcdfaa578cfb7/67003076/video/tos/useast2a/tos-useast2a-pve-0068/oAEDlrQ8TnA1EBUfPMBBD8PAE2JFvQBISQfFRU/?a=1233&bti=M0BzMzU8OGYpNzo5Zi5wIzEuLjpkNDQwOg%3D%3D&ch=0&cr=13&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C&br=534&bt=267&cs=0&ds=1&ft=rO54i0z112NJYOcyUNxRNPvE86~O_5ByXsnzXtG&mime_type=video_mp4&qs=0&rc=ZTZlOzc6Z2U4MzY8OmQ5ZUBpM2p5bng5cmpvcDMzNzczM0AtLmBeMmFiNV4xYWNgXmAyYSNebGhjMmQ0LWtgLS1kMTZzcw%3D%3D&vvpl=1&l=20241004121335117415D78073888893A4&btag=e00088000&cc=3"
            },
            {
                "comment": 0,
                "created": 1705988159,
                "desc": "",
                "download": 107,
                "like": 2,
                "pageUrl": "https://www.tiktok.com/@asking.ang/video/o0lmIvIEADEL8QmlmU9BfFE8ABJW1ESfR1rn3C",
                "playing": 107,
                "poster": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oYJBrjSA61nDjf8gAcYRD1fAEIBFvUElQEmI8t~tplv-tiktokx-cropcenter-q:300:400:q72.jpeg?dr=14782&nonce=20394&refresh_token=456d48636457bbad141b231794afb909&x-expires=1728129600&x-signature=lcjPJ5xT8MApOoMKI3Sk%2FUYjtk0%3D&biz_tag=tt_video&idc=maliva&ps=933b5bde&s=PUBLISH&sc=cover&shcp=132edbea&shp=d05b14bd&t=bacd0480",
                "share": 0,
                "videoUrl": "https://v16m.tiktokcdn.com/97476b2dc15ba484b34db8900b053d2e/6700305c/video/tos/useast2a/tos-useast2a-ve-0068c002/o0lmIvIEADEL8QmlmU9BfFE8ABJW1ESfR1rn3C/?a=1233&bti=M0BzMzU8OGYpNzo5Zi5wIzEuLjpkNDQwOg%3D%3D&ch=0&cr=13&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C&cv=1&br=204&bt=102&cs=0&ds=6&ft=rO54i0z112NJYOcyUNxRNPvE86~O_5ByXsnzXtG&mime_type=video_mp4&qs=0&rc=NDk6NGY2OWc7aWVoOjk8NkBpMzt5bng5cmdvcDMzNzczM0AwLzAvNWJfNi4xYzZgNDU0YSNnbGhjMmRjLWtgLS1kMTZzcw%3D%3D&vvpl=1&l=20241004121335117415D78073888893A4&btag=e00088000&cc=3"
            },
            {
                "comment": 0,
                "created": 1705988147,
                "desc": "",
                "download": 93,
                "like": 5,
                "pageUrl": "https://www.tiktok.com/@asking.ang/video/ogwL6AfsJrEQEURaE8QHIfFEPOEtOlvFDFB0Bk",
                "playing": 93,
                "poster": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/o0egAVvQdfnoFZWQgvTzRegTeYRG4NA0GDED6k~tplv-tiktokx-cropcenter-q:300:400:q72.jpeg?dr=14782&nonce=4128&refresh_token=ee3e73d0ed5763649640d9a0595ebe1d&x-expires=1728129600&x-signature=ZpBLDhBmaxBGe8P5WlQOQjhcAik%3D&biz_tag=tt_video&idc=maliva&ps=933b5bde&s=PUBLISH&sc=cover&shcp=132edbea&shp=d05b14bd&t=bacd0480",
                "share": 0,
                "videoUrl": "https://v16m.tiktokcdn.com/9e2e3bf1c3033c9f69c584bd5aec0940/67003084/video/tos/useast2a/tos-useast2a-pve-0068/ogwL6AfsJrEQEURaE8QHIfFEPOEtOlvFDFB0Bk/?a=1233&bti=M0BzMzU8OGYpNzo5Zi5wIzEuLjpkNDQwOg%3D%3D&ch=0&cr=13&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C&br=1328&bt=664&cs=0&ds=6&ft=rO54i0z112NJYOcyUNxRNPvE86~O_5ByXsnzXtG&mime_type=video_mp4&qs=0&rc=PDY5aWQ0ODMzaDk2OTk8OEBpM2dpd3c5cmlucDMzNzczM0AvMDNeLjUtX2IxMF4yMGEvYSMvc2QvMmQ0bGtgLS1kMTZzcw%3D%3D&vvpl=1&l=20241004121335117415D78073888893A4&btag=e00088000&cc=3"
            },
            {
                "comment": 0,
                "created": 1705987131,
                "desc": "",
                "download": 4,
                "like": 0,
                "pageUrl": "https://www.tiktok.com/@asking.ang/video/o4AiCIILSI1AMj1Rc8eeCLmXKGvBtpgLAed1xg",
                "playing": 4,
                "poster": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/ogIQBPlvLAAiydcEZm9UaB7vTSiEXDVUQ2icm~tplv-tiktokx-cropcenter-q:300:400:q72.jpeg?dr=14782&nonce=59668&refresh_token=9546917d917174b2207a540b0d3d111a&x-expires=1728129600&x-signature=z0Yb5wrH2gI4OLTNGLZWMrAft%2Bo%3D&biz_tag=tt_video&idc=maliva&ps=933b5bde&s=PUBLISH&sc=cover&shcp=132edbea&shp=d05b14bd&t=bacd0480",
                "share": 0,
                "videoUrl": "https://v16m.tiktokcdn.com/d5bf319dd02fdbe9b1ac665a04ebae6f/67003078/video/tos/useast2a/tos-useast2a-ve-0068c001/o4AiCIILSI1AMj1Rc8eeCLmXKGvBtpgLAed1xg/?a=1233&bti=M0BzMzU8OGYpNzo5Zi5wIzEuLjpkNDQwOg%3D%3D&ch=0&cr=13&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C&br=1254&bt=627&cs=0&ds=6&ft=rO54i0z112NJYOcyUNxRNPvE86~O_5ByXsnzXtG&mime_type=video_mp4&qs=0&rc=OGlpZDxoPGY3aDs0PGU8PEBpampvcWw5cjlucDMzNzczM0AuNmFeNjZhNl8xMi5fY19hYSM0YjBxMmRra2tgLS1kMTZzcw%3D%3D&vvpl=1&l=20241004121335117415D78073888893A4&btag=e00088000&cc=3"
            },
            {
                "comment": 0,
                "created": 1705986957,
                "desc": "",
                "download": 2,
                "like": 0,
                "pageUrl": "https://www.tiktok.com/@asking.ang/video/osgeRACTjlRXA4MLeXqf88nUYYwIhQEgSLpyCo",
                "playing": 2,
                "poster": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/o8xgUeShAeYIpwSLjJMCCLRB4QQUIAXvuifX8M~tplv-tiktokx-cropcenter-q:300:400:q72.jpeg?dr=14782&nonce=61303&refresh_token=06e3a22d49a9b91dcd64289b66e87839&x-expires=1728129600&x-signature=aBZNQs6j8IIQbqtzzCY5zNzexyY%3D&biz_tag=tt_video&idc=maliva&ps=933b5bde&s=PUBLISH&sc=cover&shcp=132edbea&shp=d05b14bd&t=bacd0480",
                "share": 0,
                "videoUrl": "https://v16m.tiktokcdn.com/54def059772798a1faffd5b4409d585f/6700305d/video/tos/useast2a/tos-useast2a-pve-0068/osgeRACTjlRXA4MLeXqf88nUYYwIhQEgSLpyCo/?a=1233&bti=M0BzMzU8OGYpNzo5Zi5wIzEuLjpkNDQwOg%3D%3D&ch=0&cr=13&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C&br=1264&bt=632&cs=0&ds=6&ft=rO54i0z112NJYOcyUNxRNPvE86~O_5ByXsnzXtG&mime_type=video_mp4&qs=0&rc=OzlnZDM3Zzc3Nmc2aWU5OEBpM3lrc3g5cjducDMzNzczM0A1YGJfMmIvXzQxNTMzYF42YSMwMjUwMmQ0amtgLS1kMTZzcw%3D%3D&vvpl=1&l=20241004121335117415D78073888893A4&btag=e00088000&cc=3"
            },
            {
                "comment": 0,
                "created": 1702586639,
                "desc": "",
                "download": 2,
                "like": 0,
                "pageUrl": "https://www.tiktok.com/@asking.ang/video/oYImbjCK0e7aiFJ9ej9DRgNIS0CfAaF6YEaME2",
                "playing": 2,
                "poster": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/o0E7YzjIECAfQIp7AKZgMjFJSCFi0aeD2t7aCe~tplv-tiktokx-cropcenter-q:300:400:q72.jpeg?dr=14782&nonce=16612&refresh_token=2cab3e5a43f60be6a36ed57e01ae86aa&x-expires=1728129600&x-signature=%2B3YkJMA6llAqoaBRQZo8wddvNds%3D&biz_tag=tt_video&idc=maliva&ps=933b5bde&s=PUBLISH&sc=cover&shcp=132edbea&shp=d05b14bd&t=bacd0480",
                "share": 0,
                "videoUrl": "https://v16m.tiktokcdn.com/a499820c90b787e6489efe63df6a8cfd/6700305a/video/tos/useast2a/tos-useast2a-pve-0068/oYImbjCK0e7aiFJ9ej9DRgNIS0CfAaF6YEaME2/?a=1233&bti=MzU8OGYpNHYpNzo5ZjEuLjpkLTptNDQwOg%3D%3D&ch=0&cr=13&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C&br=1372&bt=686&cs=0&ds=6&ft=rO54i0z112NJYOcyUNxRNPvE86~O_5ByXsnzXtG&mime_type=video_mp4&qs=0&rc=ZWc1NTY3OmVoaDQ6OTM1OEBpam4zbXg5cjlwbzMzNzczM0AyNjU2Xl8zNTYxNDViMmFfYSNlZzAvMmRrZXFgLS1kMTZzcw%3D%3D&vvpl=1&l=20241004121335117415D78073888893A4&btag=e00088000&cc=3"
            },
            {
                "comment": 0,
                "created": 1691494097,
                "desc": "#\ud83d\ude07",
                "download": 0,
                "like": 0,
                "pageUrl": "https://www.tiktok.com/@asking.ang/video/ocHaQtGAzgzyfL3COShJR7ItaAkET76oEkIcNA",
                "playing": 0,
                "poster": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oImIZRNBBnT0vJ0k42eGQaQDRAIeCKdbEJBkvi~tplv-tiktokx-cropcenter-q:300:400:q72.jpeg?dr=14782&nonce=35640&refresh_token=acbdea8297e722222150cf18b3d80b8b&x-expires=1728129600&x-signature=pp7vw1HdL%2BXaIsKoAb%2FHi3qaShM%3D&biz_tag=tt_video&idc=maliva&ps=933b5bde&s=PUBLISH&sc=cover&shcp=132edbea&shp=d05b14bd&t=bacd0480",
                "share": 0,
                "videoUrl": "https://v16m.tiktokcdn.com/f33da33df1b2f7f8ecc3fe81f2d55598/6700307f/video/tos/maliva/tos-maliva-ve-0068c801-us/ocHaQtGAzgzyfL3COShJR7ItaAkET76oEkIcNA/?a=1233&bti=M0BzMzU8OGYpNzo5Zi5wIzEuLjpkNDQwOg%3D%3D&ch=0&cr=13&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C&br=2482&bt=1241&cs=0&ds=6&ft=rO54i0z112NJYOcyUNxRNPvE86~O_5ByXsnzXtG&mime_type=video_mp4&qs=0&rc=ZWc6Z2Q0NWQ8aGY1OWY7aEBpajl5ajc6Zjo1bTMzNzczM0AyNjBfY2AuNTUxMTVhLy1iYSNxaDM2cjRfYTZgLS1kMTZzcw%3D%3D&vvpl=1&l=20241004121335117415D78073888893A4&btag=e00088000&cc=3"
            }
        ],
        "likes": 7,
        "pictureUrl": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/2ef0f943669bd6672a6131315b38cf31~c5_1080x1080.jpeg?lk3s=a5d48078&nonce=80056&refresh_token=2e3eb784bbec45969804728f5c54b230&x-expires=1728216000&x-signature=OfegRYR6bu3BXawAV35kgRG3VQQ%3D&shp=a5d48078&shcp=2472a6c6",
        "private": false,
        "profileUrl": "https://www.tiktok.com/@asking.ang",
        "relation": 0,
        "secretId": "MS4wLjABAAAA7dla7b2cQ9YB1GQnz7KuXDKEf37BncUIue2lh9dgoL7PjBjmofbkPB9DgR67Ki7f",
        "social": {
            "instagram": "",
            "twitter": "",
            "youtube": ""
        },
        "username": "asking.ang",
        "verified": false,
        "videos": 8,
        "website": null
    },
    "status": 200
}

'''