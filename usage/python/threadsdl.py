import requests
import json

endpoint = 'https://execross.com/api/v3/threadsdl'
headers = {
    'apikey': 'forexecman'
}
params = {
    'url': 'https://www.threads.net/@albina.capoeira_/post/DBbINETNmtS?xmt=AQGzdyw_SZghHDLL8LeUuNp-2kiH65k1bk9BWuA7jGdafA'
}
try:
    response = requests.get(endpoint, params=params, headers=headers).json()
    if response['status'] == 200:
        print("Response:", json.dumps(response, indent=4))
    else:
        print("Status Code:", response['status'])

except Exception as e:
    print("An error occurred:", str(e))


''' 
Response: {
    "creator": "EXECROSS",
    "ip": "182.1.67.220",
    "result": {
        "caption": "Snap ?\n2006\ud83e\udd75",
        "media": [
            {
                "type": "image",
                "url": "https://cdn.threadsphotodownloader.com/scontent-lga3-1.cdninstagram.com/v/t51.29350-15/464378461_1959232707910400_3174110970616917121_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=18de74&_nc_ohc=QtONIvKZRoUQ7kNvgEy78E0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=AhGIi018S--yVT-cxjalhtY&oh=00_AYDL_61FxAURq6O1QvATCOmSxaYpnaK4cWeNhJUvyBJYjA&oe=671E2B3D"
            },
            {
                "type": "video",
                "url": "https://cdn.threadsphotodownloader.com/scontent-lga3-1.cdninstagram.com/o1/v/t16/f2/m69/AQM2NMy_ymT3jsNPOv68bnfOG7blyFImHtfjLxVWjKofgg2kI94_LtjBT9ZWMCVpMzV2tMkGibjP3gy_VFfcLwEi?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLmNhcm91c2VsX2l0ZW0udW5rbm93bi1DMi43MjAuZGFzaF9iYXNlbGluZV8xX3YxIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=102&vs=8582092275166992_2648841336&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTTNxcVJ1R01IS29rRVlGQUR1MTNqZlBwUmNMYmtZTEFBQUYVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dBN2pxeHNiVTlhVEY5UUZBRmd5cEtBejI4Smdia1lMQUFBRhUCAsgBACgAGAAbAYgHdXNlX29pbAExFQAAJri9muT08rc%2FFQIoAkMzLBdAJQAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB17gcA&ccb=9-4&oh=00_AYDD6tezM05JqQsJqHyta-bE9SFq1AfUPkus7ZGIaFi1VQ&oe=671A4686&_nc_sid=1d576d"      
        ],
        ],
        "page": "https://www.threads.net/@albina.capoeira_/post/DBbINETNmtS?xmt=AQGzdyw_SZghHDLL8LeUuNp-2kiH65k1bk9BWuA7jGdafA",
        "picture": "https://downloads.acxcdn.com/threadster/image?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJodHRwczovL3Njb250ZW50LmNkbmluc3RhZ3JhbS5jb20vdi90NTEuMjg4NS0xOS80NjQzNDYwMjJfMTA4NDczODc2OTk1MTExMl82NTAyMDE2OTYxNDY4MzAwNDczX24uanBnP3N0cD1kc3QtanBnX3MxMDB4MTAwJl9uY19jYXQ9MSZjY2I9MS03Jl9uY19zaWQ9YmY3ZWI0Jl9uY19vaGM9M093NGtqQ1k0RW9RN2tOdmdIWkRxZHgmX25jX3p0PTI0Jl9uY19odD1zY29udGVudC5jZG5pbnN0YWdyYW0uY29tJm9oPTAwX0FZQkpmZ2R2ZEFjek5EbEs3dW9nSnI5WHdwczdUeFZCRTNuR2pnUHBDZGQxckEmb2U9NjcxRTRDREYiLCJpYXQiOjE3Mjk2NTU0Nzl9.CjuHrBdrzvfy_QdgRO01uWBfR-83a-vlWYpDxq0uzds",
        "username": "@albina.capoeira_"
    },
    "status": 200
}

'''