import requests,json

endpoint = 'https://execross.com/api/v3/tweetprofile'
headers = {
    'apikey': 'forexecman'
}
params = {
    "userid" : "0xangx",
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
if responsed['status'] == 200:
    print("Response:",json.dumps(responsed,indent=4))
else:
    print(responsed)

'''
Response will be:

Response: {
    "creator": "EXECROSS",
    "ip": "182.1.82.58",
    "result": {
        "__typename": "User",
        "affiliates_highlighted_label": {},
        "has_nft_avatar": false,
        "id": "VXNlcjoxNTg3NjU3MDk5NDA3ODA2NDY0",
        "is_profile_translatable": false,
        "legacy": {
            "blocked_by": false,
            "blocking": false,
            "can_dm": false,
            "can_media_tag": true,
            "created_at": "Wed Nov 02 04:05:42 +0000 2022",
            "default_profile": true,
            "default_profile_image": false,
            "description": "Learn until rekt!",
            "entities": {
                "description": {
                    "urls": []
                }
            },
            "fast_followers_count": 0,
            "favourites_count": 28,
            "follow_request_sent": false,
            "followed_by": false,
            "followers_count": 36,
            "following": false,
            "friends_count": 97,
            "has_custom_timelines": false,
            "is_translator": false,
            "listed_count": 0,
            "location": "",
            "media_count": 36,
            "muting": false,
            "name": "ahoBaka",
            "normal_followers_count": 36,
            "notifications": false,
            "pinned_tweet_ids_str": [],
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/1591026404333735936/84nbd_KB_normal.jpg",
            "profile_interstitial_type": "",
            "protected": false,
            "screen_name": "0xangx",
            "statuses_count": 286,
            "translator_type": "none",
            "verified": false,
            "want_retweets": false,
            "withheld_in_countries": []
        },
        "legacy_extended_profile": {},
        "rest_id": "1587657099407806464",
        "smart_blocked_by": false,
        "smart_blocking": false,
        "super_follow_eligible": false,
        "super_followed_by": false,
        "super_following": false
    },
    "status": 200
}
'''