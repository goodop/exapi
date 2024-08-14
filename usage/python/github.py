import requests,json

endpoint = 'https://execross.com/api/v3/github'
headers = {
    'apikey': 'forexecman'
}
params = {
    "username" : "goodop",
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
if responsed['status'] == 200:
    print("Response:",json.dumps(responsed,indent=4))
else:
    print(responsed['message'])

'''
Response: {
    "creator": "EXECROSS",
    "ip": "182.1.91.138",
    "result": {
        "avatar_url": "https://avatars.githubusercontent.com/u/54814225?v=4",
        "bio": "Normal temperature \ud83e\uddbe\ud83e\udd16",
        "blog": "ang.execross.com",
        "company": "imjustgood.com",
        "created_at": "2019-09-02T16:48:50Z",
        "email": "angexecross@gmail.com",
        "followers": 35,
        "following": 5,
        "gravatar_id": "",
        "hireable": null,
        "html_url": "https://github.com/goodop",
        "id": 54814225,
        "location": "Surabaya, Great Indonesia",
        "login": "goodop",
        "name": "Ang",
        "node_id": "MDQ6VXNlcjU0ODE0MjI1",
        "organizations_url": "https://api.github.com/users/goodop/orgs",
        "public_gists": 0,
        "public_repos": 12,
        "repos_url": "https://api.github.com/users/goodop/repos",
        "site_admin": false,
        "subscriptions_url": "https://api.github.com/users/goodop/subscriptions",
        "twitter_username": "0xangx",
        "type": "User",
        "updated_at": "2024-08-04T07:35:43Z",
        "url": "https://api.github.com/users/goodop"
    },
    "status": 200
}
'''