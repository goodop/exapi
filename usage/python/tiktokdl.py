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
    "ip": "46.27.15.132",
    "result": {
        "ai_dynamic_cover": "https://p16-sign-va.tiktokcdn.com/obj/tos-maliva-p-0068/2e21a623eea44d4e8a86beacbfa29eb6_1715479326?lk3s=d05b14bd&nonce=32604&refresh_token=bd73c5e62b92a3bba10f92ad845450ee&x-expires=1722610800&x-signature=j6STbKhOXsadsR2I2lZm9z6EtcY%3D&s=AWEME_DETAIL&se=false&sh=&sc=dynamic_cover&l=20240801155329945CC0CB7B84FF1A4ABE&shp=d05b14bd&shcp=-",
        "anchors": null,
        "anchors_extras": "",
        "author": {
            "avatar": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/2cbdfc7d16623c36b90207431d183c56~c5_300x300.jpeg?lk3s=45126217&nonce=55230&refresh_token=bc0830fe901ea1b711b72096f9b3277a&x-expires=1722610800&x-signature=a660%2F1VXxyx0iDvB8QFUtY8wDyQ%3D&shp=45126217&shcp=-",
            "id": "6744619110091867138",
            "nickname": "\ud835\udc68\ud835\udc94\ud835\udc89\ud835\udc82\ud835\udc83\ud835\udc96\ud835\udc8d \ud835\udc72\ud835\udc82\ud835\udc89\ud835\udc87\ud835\udc8a",
            "unique_id": "islamicvibes1445"
        },
        "collect_count": 5339,
        "comment_count": 69,
        "commerce_info": {
            "adv_promotable": false,
            "auction_ad_invited": false,
            "branded_content_type": 0,
            "with_comment_filter_words": false
        },
        "commercial_video_info": "",
        "cover": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oEzoA48UjxQIBiAjokAhE6viSI6ZB9ZAsAbEA~c5_300x400.jpeg?lk3s=d05b14bd&nonce=86308&refresh_token=82eb61b4ffcb203b2f4e3d73054b2ca2&x-expires=1722610800&x-signature=Vc6yWiL1yLjUcLLjwAa7v2RVRSQ%3D&s=AWEME_DETAIL&se=false&sh=&sc=cover&l=20240801155329945CC0CB7B84FF1A4ABE&shp=d05b14bd&shcp=-",
        "create_time": 1715479322,
        "digg_count": 24101,
        "download_count": 3542,
        "duration": 13,
        "id": "7367927569280240901",
        "is_ad": false,
        "item_comment_settings": 0,
        "music": "https://sf16-ies-music-sg.tiktokcdn.com/obj/tiktok-obj/7213421030067440386.mp3",
        "music_info": {
            "album": "",
            "author": "scars",
            "cover": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/tiktok_user_default_avatar~c5_1080x1080.jpeg?lk3s=45126217&nonce=56702&refresh_token=ed99763db793afe4ee0ea28fc79eaad9&x-expires=1722610800&x-signature=XPgwybXbs5cuWCT29MCwEUjGTzo%3D&shp=45126217&shcp=-",
            "duration": 44,
            "id": "7213421053140339457",
            "original": true,
            "play": "https://sf16-ies-music-sg.tiktokcdn.com/obj/tiktok-obj/7213421030067440386.mp3",
            "title": "Everything Works Out in the end instrumental"
        },
        "origin_cover": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/f027a1f92ccf4574a141c57980866df5_1715479324~tplv-tiktokx-360p.image?lk3s=d05b14bd&nonce=92513&refresh_token=93cc87a02aa61124d14d0df76a8b18d0&x-expires=1722610800&x-signature=PwbjbzxI%2FMFNkdxY2KHzrK1OTgw%3D&s=AWEME_DETAIL&se=false&sh=&sc=feed_cover&l=20240801155329945CC0CB7B84FF1A4ABE&shp=d05b14bd&shcp=-",
        "play": "https://v16m-default.akamaized.net/2da0f9a6060d756e84aab364c26d333e/66ac03e7/video/tos/useast2a/tos-useast2a-ve-0068c001/okE8A6xivhj09AQJpSCEIzB9BIhAUAjAUqikZ/?a=0&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=208&bt=104&cs=0&ds=6&ft=XE5bCqT0majPD12Fq4-73wUOx5EcMeF~O5&mime_type=video_mp4&qs=0&rc=NzM8NDs2M2U1NDUzNTM8aUBpM206O3Y5cjM1czMzNzczM0BeNS82X2E2XmExYS0xXl4tYSNxb3AtMmRrMy1gLS1kMTZzcw%3D%3D&vvpl=1&l=20240801155329945CC0CB7B84FF1A4ABE&btag=e00088000",
        "play_count": 388791,
        "region": "ID",
        "share_count": 2618,
        "size": 174610,
        "title": "Besok adalah Mystery\u2728#quotes #quotesislam ",
        "wm_size": 161417,
        "wmplay": "https://v16m-default.akamaized.net/1338a15644fb80cd8a88114110dccef5/66ac03e7/video/tos/useast2a/tos-useast2a-pve-0068/ocmRJPABCBnQCAFR4B7IHZNE7QEDQffKZMXDE0/?a=0&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=192&bt=96&cs=0&ds=6&ft=XE5bCqT0majPD12Fq4-73wUOx5EcMeF~O5&mime_type=video_mp4&qs=11&rc=PDRnNDQ6ZDxkN2RkZDNlZEBpM206O3Y5cjM1czMzNzczM0AwLy9jYmAyXzExMzNgNjUtYSNxb3AtMmRrMy1gLS1kMTZzcw%3D%3D&vvpl=1&l=20240801155329945CC0CB7B84FF1A4ABE&btag=e00088000"
    },
    "status": 200
}

"""
