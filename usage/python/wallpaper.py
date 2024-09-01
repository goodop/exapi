import requests
import json


url = 'https://execross.com/api/v3/wallpaper'
headers = {
	"apikey": "forexecman"
}
params = {
	"query":"city"
}
datas = requests.get(url,headers=headers,params=params).json()
response = json.dumps(datas,indent=4)
print(response)


'''
Response will be:
{
    "creator": "EXECROSS",
    "ip": "125.164.1.154",
    "result": [
        "https://cdn.bhdw.net/im/happy-students-wallpaper-125102_w635.webp",
        "https://cdn.bhdw.net/im/spider-man-into-the-verse-mcu-wallpaper-125078_w635.webp",
        "https://cdn.bhdw.net/im/lonely-girl-at-city-top-building-wallpaper-125076_w635.webp",
        "https://cdn.bhdw.net/im/lonely-anime-girl-wallpaper-125045_w635.webp",
        "https://cdn.bhdw.net/im/outside-the-city-wallpaper-125002_w635.webp",
        "https://cdn.bhdw.net/im/spider-gwen-in-new-york-wallpaper-124983_w635.webp",
        "https://cdn.bhdw.net/im/girl-in-the-desert-city-1-wallpaper-124967_w635.webp",
        "https://cdn.bhdw.net/im/cybertown1-wallpaper-124957_w635.webp",
        "https://cdn.bhdw.net/im/intense-excitement-of-a-high-tech-motorcycle-in-a-neon-city-wallpaper-124717_w635.webp",
        "https://cdn.bhdw.net/im/neon-rush-of-a-sleek-motorcycle-in-a-futuristic-city-wallpaper-124716_w635.webp",
        "https://cdn.bhdw.net/im/bustling-energy-of-a-vintage-motorcycle-in-a-colorful-city-wallpaper-124715_w635.webp",
        "https://cdn.bhdw.net/im/dynamic-streets-of-a-colorful-city-with-a-vintage-motorcycle-wallpaper-124714_w635.webp",
        "https://cdn.bhdw.net/im/playful-energy-of-a-vintage-motorcycle-in-the-city-wallpaper-124712_w635.webp",
        "https://cdn.bhdw.net/im/city-skyline-feature-wallpaper-124678_w635.webp",
        "https://cdn.bhdw.net/im/vibrant-city-life-a-watercolor-symphony-of-colors-wallpaper-124664_w635.webp",
        "https://cdn.bhdw.net/im/cyberpunk-city-streets-wallpaper-124633_w635.webp",
        "https://cdn.bhdw.net/im/cyberpunk-city-at-night-wallpaper-124632_w635.webp",
        "https://cdn.bhdw.net/im/cyborg-cop-in-cyberpunk-wallpaper-124630_w635.webp",
        "https://cdn.bhdw.net/im/cyberpunk-cop-wallpaper-124629_w635.webp",
        "https://cdn.bhdw.net/im/a-bentley-continental-gt-parked-on-a-bustling-london-street-wallpaper-124563_w635.webp",
        "https://cdn.bhdw.net/im/amy-jackson-l-officiel-uk-magazine-shoot-wallpaper-124333_w635.webp"        
    ],
    "status": 200
}
'''