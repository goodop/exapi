import requests
import json

base_url = 'https://execross.com/api/v3'
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey, 'Content-Type': 'application/json'})

def getTiktokPost():
    url = f"{base_url}/tiktokdl"
    params = {
       "url":  "https://vt.tiktok.com/ZSYwxGV9P/"
    }
    response = session.get(url, params=params).json()
    data = json.dumps(response, indent=4)
    print("Response: ", data)


getTiktokPost()

""" 
Respon Will be:

Response:  {
    "creator": "EXECROSS",
    "ip": "61.5.71.228",
    "result": {
        "caption": "Besok adalah Mystery\u2728#quotes #quotesislam ",   
        "comment": "75",
        "covertrack": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/2e21a623eea44d4e8a86beacbfa29eb6_1715479326~tplv-tiktokx-origin.image?dr=14575&nonce=32558&refresh_token=e5b26a5672ab7618d51ef381bf3a4b4c&x-expires=1728108000&x-signature=3f5ilT4W5xhYG5ZSYS8nqJ%2F3mnQ%3D&idc=maliva&ps=13740610&s=AWEME_DETAIL&shcp=34ff8df6&shp=d05b14bd&t=4d5b0474",    
        "created": "1970-01-01 00:00:00",
        "download": "4159",
        "duration": "13",
        "fullname": "\ud835\udc68\ud835\udc94\ud835\udc89\ud835\udc82\ud835\udc83\ud835\udc96\ud835\udc8d \ud835\udc72\ud835\udc82\ud835\udc89\ud835\udc87\ud835\udc8a",
        "id": "7367927569280240901",
        "images": [],
        "like": "27608",
        "mention": "",
        "music": "Everything Works Out in the end instrumental",        
        "musicInfo": {
            "album": "",
            "author": "scars",
            "cover": "https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/1594805258216454~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=14579&nonce=11325&refresh_token=214b547436ab72e9d46d2e78a8cdb69c&x-expires=1728108000&x-signature=IomBPJRqqqC5T%2Bj6ft%2FhyVXyxb8%3D&idc=maliva&ps=13740610&shcp=d05b14bd&shp=45126217&t=4d5b0474",
            "duration": 44,
            "id": "7213421053140339457",
            "original": true,
            "play": "https://sf16-ies-music-sg.tiktokcdn.com/obj/tiktok-obj/7213421030067440386.mp3",
            "title": "Everything Works Out in the end instrumental"     
        },
        "no_watermark": "https://v16m-default.akamaized.net/7a42b7e21ac3a4b1d6c8d15f98b6e41a/66ffe1a2/video/tos/useast2a/tos-useast2a-ve-0068c001/okE8A6xivhj09AQJpSCEIzB9BIhAUAjAUqikZ/?a=0&bti=OTg7QGo5QHM6OjZALTAzYCMvcCMxNDNg&ch=0&cr=0&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C0&cv=1&br=208&bt=104&cs=0&ds=6&ft=XE5bCqT0majPD12Tzpp73wUOx5EcMeF~O5&mime_type=video_mp4&qs=0&rc=NzM8NDs2M2U1NDUzNTM8aUBpM206O3Y5cjM1czMzNzczM0BeNS82X2E2XmExYS0xXl4tYSNxb3AtMmRrMy1gLS1kMTZzcw%3D%3D&vvpl=1&l=20241004063739E05A4FA530EB7C720A44&btag=e00088000",
        "picture": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/2cbdfc7d16623c36b90207431d183c56~tplv-tiktokx-cropcenter:300:300.jpeg?dr=14577&nonce=42188&refresh_token=38443fee65252189bbe4a95884453f4a&x-expires=1728108000&x-signature=Yxpn3VB7iFuQyikgc5lO28Me6ac%3D&idc=maliva&ps=13740610&shcp=d05b14bd&shp=45126217&t=4d5b0474",
        "play": "449049",
        "region": "ID",
        "share": "3052",
        "sound": "https://sf16-ies-music-sg.tiktokcdn.com/obj/tiktok-obj/7213421030067440386.mp3",
        "thumbnail": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/f027a1f92ccf4574a141c57980866df5_1715479324~tplv-tiktokx-360p.image?dr=14555&nonce=90955&refresh_token=3eaa1516b62e968d17a9212b3b31cc79&x-expires=1728108000&x-signature=E7g22qt94cNdA0MunZWwQxf47p4%3D&ftpl=1&idc=maliva&ps=13740610&s=AWEME_DETAIL&shcp=34ff8df6&shp=d05b14bd&t=4d5b0474",  
        "username": "islamicvibes1445",
        "videoSize": 174610,
        "watermark": "https://v16m-default.akamaized.net/92fdcaebb625155fb0ed19b7804c59f3/66ffe1a2/video/tos/useast2a/tos-useast2a-pve-0068/ocmRJPABCBnQCAFR4B7IHZNE7QEDQffKZMXDE0/?a=0&bti=OTg7QGo5QHM6OjZALTAzYCMvcCMxNDNg&ch=0&cr=0&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C0&cv=1&br=192&bt=96&cs=0&ds=6&ft=XE5bCqT0majPD12Tzpp73wUOx5EcMeF~O5&mime_type=video_mp4&qs=11&rc=PDRnNDQ6ZDxkN2RkZDNlZEBpM206O3Y5cjM1czMzNzczM0AwLy9jYmAyXzExMzNgNjUtYSNxb3AtMmRrMy1gLS1kMTZzcw%3D%3D&vvpl=1&l=20241004063739E05A4FA530EB7C720A44&btag=e00088000"
    },
    "status": 200
}

"""
