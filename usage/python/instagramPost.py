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
    'url': 'https://www.instagram.com/p/CMZ8rozlRXD/?igsh=MWdyaXRmaXp0bThxNg==' # Instagram Post, Reels / IGTV
    }
    response = session.get(url, params=params).json()
    data = json.dumps(response, indent=4)
    print("Response: ", data)


fetIGPost()

'''
Response:  {
    "creator": "EXECROSS",
    "ip": "182.1.82.58",
    "result": {
        "data": [
            "https://d.snapcdn.app/saveinsta?file=eyJ1cmwiOiJodHRwczovL3Njb250ZW50LmNkbmluc3RhZ3JhbS5jb20vdi90NTEuMjkzNTAtMTUvMTYwMDY1OTU5XzI1ODIxMzQ0NTk3MDg0NV8zNTI2OTI4MzEzMDA1ODEyNjhfbi5qcGc_c2U9NyZzdHA9ZHN0LWpwZ19lMzUmZWZnPWV5SjJaVzVqYjJSbFgzUmhaeUk2SW1sdFlXZGxYM1Z5YkdkbGJpNHhNRGd3ZURFd09EQXVjMlJ5TG1ZeU9UTTFNQ0o5Jl9uY19odD1zY29udGVudC1hbXM0LTEuY2RuaW5zdGFncmFtLmNvbSZfbmNfY2F0PTEwMSZfbmNfb2hjPVdtLUhVT2syUGJnUTdrTnZnRno1dUFTJmVkbT1BUF9WMTBFQkFBQUEmY2NiPTctNSZvaD0wMF9BWUNyd1RneFhNU2FUeE9yQjBtV0Jaekk4TkxnRVpFRVExU1VzU1RTVFZxT0x3Jm9lPTY2QkZBNUM4Jl9uY19zaWQ9Mjk5OWI4IiwiZmlsZW5hbWUiOiJTYXZlSW5zdGEuQXBwXzE2MDA2NTk1OV8yNTgyMTM0NDU5NzA4NDVfMzUyNjkyODMxMzAwNTgxMjY4X24uanBnIiwiZXhwaXJlcyI6MTcyMzQ2NTUzMywidG9rZW4iOiJmNGZiYzI4MjhhMDZjMTc5NzcyYTE3OTQ4Y2RjYTFjZDY1YWMwNTFhMzFiNzhlNzEwNmVmN2Y5Mjc3YjM1YjZjIn0"
        ]
    },
    "status": 200
}
'''