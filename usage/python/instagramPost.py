import requests
import json

base_url = 'https://execross.com/api/v3'
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey, 'Content-Type': 'application/json'})

def fetIGPost():
    url = f"{base_url}/instapost"
    params = {
    'apikey': apikey,
    'url': 'https://www.instagram.com/p/DBap45xz3pb/?igsh=dTZsMjRicmdtOHM5' # Instagram Post, Reels / IGTV
    }
    response = session.get(url, params=params).json()
    data = json.dumps(response, indent=4)
    print("Response: ", data)


fetIGPost()

'''
Response:  {
    "creator": "EXECROSS",
    "ip": "182.1.67.220",
    "result": {
        "caption": "Tentara Nasional Indonesia Angkatan Udara (TNI AU) mengerahkan delapan pesawat tempurnya mengawal penerbangan Presiden Ke-7 RI Joko Widodo (Jokowi) ke Solo, Jawa Tengah, Minggu (20/10/2024) sore.\n\nKepala Dinas Penerangan Angkatan Udara (Kadispenau) Marsekal Pertama TNI Ardi Syahri menjelaskan rincian pesawat tempur yang digunakan mengawal pesawat Boeing 737-800 Next Gen bernomor ekor A7309 yang ditumpangi Jokowi.\n\n\"Pengawalan kehormatan Presiden Ke-7 RI Pak Joko Widodo kembali ke Solo dari Pangkalan Udara Halim Perdanakusuma dikawal tiga pesawat T-50, empat pesawat tempur F-16, dan satu Sukhoi,\" kata Marsma TNI Ardi Syahri\n\nEmpat pesawat tempur F-16 yang mengawal penerbangan Jokowi dari Lanud Halim Perdanakusuma, Jakarta ke Solo berasal dari Skadron Udara 16 Lanud Roesmin Nurjadin. Satu pesawat tempur F-16 itu bertugas mengabadikan pesawat Boeing yang mengantarkan Jokowi kembali ke Solo ketika dikawal pesawat tempur TNI AU.\n\nSementara, tiga jet tempur latih T-50i Golden Eagle berasal dari Skadron Udara 15 Lanud Iswahjudi, Jawa Timur. Adapun satu pesawat tempur Sukhoi yang mengawal Jokowi berasal dari Skadron Udara 11 Lanud Sultan Hasanuddin.\n\n[Sumber: Kompas.com]",
        "data": [
            {
                "thumbnail": "https://scontent.cdninstagram.com/v/t51.29350-15/464358116_601342618891749_6688052851015339510_n.jpg?stp=dst-jpg_e15&_nc_ht=scontent.cdninstagram.com&_nc_cat=109&_nc_ohc=xAZR8ffdswwQ7kNvgGaRoXQ&_nc_gid=b7548d9e6d4942cb8b5623c7cf31fbb3&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYBxAC3bwBWeRBcnecPBRTEo8uc5osyhm7KR1iH00SnKDQ&oe=671E60D6&_nc_sid=10d13b",
                "type": "video",
                "url": "https://scontent.cdninstagram.com/o1/v/t16/f2/m69/AQOWT3CXtKa7Wt64iZTfo32dm4WixbP3ZczLvGQahQi0c_TGFoV_O3-sJpeSj89891mIjd28m9kPB_HMOxhDj9KJ.mp4?stp=dst-mp4&efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uY2Fyb3VzZWxfaXRlbS5jMi4xMDgwLmJhc2VsaW5lIn0&_nc_cat=110&vs=1062073252038460_3752741973&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTjFVSlJNSmgtVHNUcEVFQU54UUE4QmY5R2hqYnBSMUFBQUYVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dMNFlyQnNjSWREXzh3Y0RBTXJEZEZISzBnTWJia1lMQUFBRhUCAsgBACgAGAAbABUAACbqnNz7ubWQQBUCKAJDMywXQE4AAAAAAAAYFmRhc2hfYmFzZWxpbmVfMTA4MHBfdjERAHXuBwA%3D&_nc_rid=b754847340&ccb=9-4&oh=00_AYCY-IfAB7Weqci6iohSypSR0apxFhtbw7MA5s5mO_eFvw&oe=671A669D&_nc_sid=10d13b"
            },
            {
                "thumbnail": "https://scontent.cdninstagram.com/v/t51.29350-15/464146007_1086559849665822_7634793615274406798_n.jpg?stp=dst-jpg_e15&_nc_ht=scontent.cdninstagram.com&_nc_cat=106&_nc_ohc=ZGwrvbooRKgQ7kNvgG4tiej&_nc_gid=b7548d9e6d4942cb8b5623c7cf31fbb3&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYAizs-nvy_oY0oIoLFg0wJw4wyDyn33PPl4i2e2tg2w8A&oe=671E3638&_nc_sid=10d13b",
                "type": "video",
                "url": "https://scontent.cdninstagram.com/o1/v/t16/f2/m69/AQMyfxhQCxkdKNy8VQ0zdyyhWOgYxKP_eEW_I-1VUc72zokJT__jJ3NABHfkoHoB2mf8fCymiDO2ZId4wSyUeopA.mp4?stp=dst-mp4&efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uY2Fyb3VzZWxfaXRlbS5jMi43MjAuYmFzZWxpbmUifQ&_nc_cat=110&vs=1262167724937575_3977118491&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HSmtscFJzSkJNdmlEZXNCQU9kbHd4WkJUYm9NYmtZTEFBQUYVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dPd0RweHN5eHZyQ3YxOEVBT0NPNVhPcXFZTXpia1lMQUFBRhUCAsgBACgAGAAbABUAACbCpsWawriUQRUCKAJDMywXQE4AAAAAAAAYEmRhc2hfYmFzZWxpbmVfMV92MREAde4HAA%3D%3D&_nc_rid=b75480a1a4&ccb=9-4&oh=00_AYD4ajmpLa3xVd7JTMYfv0kpLXyN9eiXv7HG82S9GFke5A&oe=671A609F&_nc_sid=10d13b"
            },
            {
                "thumbnail": "https://scontent.cdninstagram.com/v/t51.29350-15/464235497_1939062386614692_4360325921940486457_n.jpg?stp=dst-jpg_e15&_nc_ht=scontent.cdninstagram.com&_nc_cat=100&_nc_ohc=kKJY0ga6kzQQ7kNvgEhVkPH&_nc_gid=b7548d9e6d4942cb8b5623c7cf31fbb3&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYDNuwpAG9BhEaVxbw-JQmHtoFF6wIXNBYTQdAJ35_2XrQ&oe=671E39B5&_nc_sid=10d13b",
                "type": "video",
                "url": "https://scontent.cdninstagram.com/o1/v/t16/f2/m69/AQOLSlm-TLbCfaJAHXye-ssgS2-gc1_NXudJPgK-yD-NxkcacSnUo6BMbBfq9m56VVEFqXAVwRhNeUhzAjylV1Qy.mp4?stp=dst-mp4&efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uY2Fyb3VzZWxfaXRlbS5jMi4xMDgwLmJhc2VsaW5lIn0&_nc_cat=101&vs=396521626727914_2534486519&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQkEzTGdkRXgxbWEtNE1EQUo2R21Sc0h0TGtkYnBSMUFBQUYVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dHR3RxaHRBR1E2RmtUa0VBSWpSZUJSTHNPTk5ia1lMQUFBRhUCAsgBACgAGAAbABUAACaKg8f%2Ftor8PxUCKAJDMywXQDczMzMzMzMYFmRhc2hfYmFzZWxpbmVfMTA4MHBfdjERAHXuBwA%3D&_nc_rid=b7548c3e4c&ccb=9-4&oh=00_AYBEcpJnfBt4Uef2d8hjEsi0o-xyJv__ynEOdosnpgyM-g&oe=671A512A&_nc_sid=10d13b"
            },
            {
                "type": "image",
                "url": "https://scontent.cdninstagram.com/v/t51.29350-15/464254628_1582351062681773_3860504685521204662_n.webp?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=105&_nc_ohc=19PPiCFlMP0Q7kNvgHbP1hy&_nc_gid=b7548d9e6d4942cb8b5623c7cf31fbb3&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzQ4NDI4MTQ4MTU1MDcyNTk2Nw%3D%3D.3-ccb7-5&oh=00_AYAEp8hvK-FN1z4drfrM030oY5_6gwxreqTjxjYng1nzxw&oe=671E4ACC&_nc_sid=10d13b"
            },
            {
                "type": "image",
                "url": "https://scontent.cdninstagram.com/v/t51.29350-15/464194824_1266009688163299_7791066376057994300_n.webp?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=107&_nc_ohc=UgaIeQIL0FwQ7kNvgFVBeRD&_nc_gid=b7548d9e6d4942cb8b5623c7cf31fbb3&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzQ4NDI4MTQ4MTY2ODI0NjkwNw%3D%3D.3-ccb7-5&oh=00_AYBf0t_QPstgtDjftgYBDd3TXYNjlmMdWFS8gbYDSGJipQ&oe=671E4127&_nc_sid=10d13b"
            }
        ]
    },
    "status": 200
}
'''