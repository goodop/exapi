import requests
import json


url = 'https://execross.com/api/v3/khodam'
headers = {
	"apikey": "forexecman"
}
params = {
	"name":"Bagas"
}
datas = requests.get(url,headers=headers,params=params).json()
response = json.dumps(datas,indent=4)
print(response)

'''
Respon will be:
#success (200)

{
    "creator": "EXECROSS",
    "ip": "36.74.109.56",
    "result": {
        "description": "Khodam Ikan Kocak, kekuatan air yang cepat dan manja, serupa dengan hewan air yang cerdas dan mudah beradaptasi. Ia menawarkan keberanian dan kecerdasan, mempermudah mencapai tujuan dengan cepat dan efisien. Paruhnya seperti cakrawala, mengingat makhluk astral yang bersinergi dengan air dan kekuatan intuitif. Khodam Ikan Kocak membantu mengembangkan jiwa yang fleksibel dan berani, seperti ikan yang pandai berenang dan tahan lama.",
        "khodam": "Ikan Kocak",
        "name": "Bagas",
        "poster": "https://gate.execross.com/images/khodam/014a6654-6b75-4cb9-9687-7bf97826319f.jpg",
        "title": "Khodam anda saat ini adalah Ikan Kocak"
    },
    "status": 200
}

#Failed (503)
{
    "message": "Hmm, khodam Anda tampaknya masih dalam proses pengiriman spiritual. Mungkin terjebak macet di jalan raya alam gaib.",
    "status": 503
}
'''