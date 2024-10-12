import requests
import json


url = 'https://execross.com/api/v3/bmkg'
headers = {
	"apikey": "partnerEXC"
}
datas = requests.get(url,headers=headers).json()
response = json.dumps(datas,indent=4)
print(response)

"""
{
    "creator": "EXECROSS",
    "ip": "36.74.109.56",
    "result": {
        "coordinates": "4.60 LS - 101.89 BT",
        "depth": "58 km",
        "felt": "Dirasakan (Skala MMI): III Enggano, II - III Kota Bengkulu",
        "location": "Pusat gempa berada di laut 92 km barat laut Enggano",
        "magnitude": "4.9",
        "maps": "https://www.google.com/maps/?q=-4.60,101.89",
        "poster": "https://static.bmkg.go.id/20241012083740.mmi.jpg",   
        "time": "12 Oktober 2024, 08:37:40 WIB",
        "url": "https://www.bmkg.go.id/gempabumi/gempabumi-dirasakan.bmkg"
    },
    "status": 200
}
"""