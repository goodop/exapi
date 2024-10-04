import requests
import json

endpoint = 'https://execross.com/api/v3/facebookdl'
headers = {
    'apikey': 'forexecman',
    "Content-Type": "application/json"
}
params = {
    "url": "https://www.facebook.com/share/v/gWrukhx5QRSSJukZ/?mibextid=D5vuiz"
}

response = requests.post(endpoint, params=params, headers=headers).json()
print("Response:", json.dumps(response, indent=4))

Response: {
    "creator": "EXECROSS",
    "ip": "61.5.71.228",
    "result": {
        "created": "2024-08-10",
        "description": "Cobra VS moongoose",
        "duration": "07:59",
        "extension": "mp4",
        "likes": "",
        "size": "--",
        "subscribers": "",
        "thumbnail": "https://scontent-sin6-1.xx.fbcdn.net/v/t15.5256-10/454513059_2507775536279003_7475253130280296851_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=596eb7&_nc_ohc=r2tuBIMOHzgQ7kNvgFdE8wK&_nc_ht=scontent-sin6-1.xx&_nc_gid=ApvHu_EqmUbpxMIxCoBWSMJ&oh=00_AYAp77JvkRfHeKz6eGEL4DyY_3EQmYhIHaoPd5F1xjrNag&oe=67056023",
        "title": "Cobra VS moongoose",
        "videoUrl": "https://video-sin6-1.xx.fbcdn.net/v/t42.1790-2/454359136_2142604742778116_5248309254882225576_n.mp4?_nc_cat=105&ccb=1-7&_nc_sid=55d0d3&efg=eyJybHIiOjUwMCwicmxhIjoyNDk2LCJ2ZW5jb2RlX3RhZyI6InN2ZV9zZCIsInZpZGVvX2lkIjo1MTkxNDI2MDM4OTM2MTR9&_nc_e2o=519142603893614&_nc_ohc=fKESeWdeDRcQ7kNvgHXN4R1&rl=500&vabr=278&_nc_ht=video-sin6-1.xx&_nc_gid=ATH-MRkehB0kScRN_xPAVNZ&oh=00_AYAiStqYNSegeRESh0JJXfsGAn4ZNp-UQhp1FM3tNi1D0g&oe=67054691",
        "views": "4M"
    },
    "status": 200
}