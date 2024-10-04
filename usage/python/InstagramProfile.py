import requests
import json

base_url = 'https://execross.com/api/v3'
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey, 'Content-Type': 'application/json'})

def fetIGDetails():
    url = f"{base_url}/instaprofile"
    params = {
       "userid":  "this.ang"
    }
    response = session.get(url, params=params).json()
    data = json.dumps(response, indent=4)
    print("Response: ", data)


fetIGDetails()


"""

Result will be:

Response:  {
    "creator": "EXECROSS",
    "ip": "61.5.71.228",
    "result": {
        "biography": "\ud83d\udc68\u200d\ud83d\udcbb Coding in the Quiet \ud83c\udf04 | \ud83d\udcda Exploring Algorithms | \ud83c\udf3f Nature Enthusiast | \u2615 Coffee Lover | Let's Connect and Code!",
        "biolink": [
            {
                "icon_url": "",
                "image_url": "",
                "is_pinned": false,
                "is_verified": false,
                "link_id": "17989249391326377",
                "link_type": "external",
                "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fang.execross.com%2F%3Ffbclid%3DPAZXh0bgNhZW0CMTEAAaYrO_7AAg5ftfgnRCKNrimhwyYw1HFMBvB8eXPMyO7FC_VDrR2canZ--O4_aem_NTm62iuOlv5gwVniBJEfDg&e=AT2FrsRaFfZJ_am7_cRyIW264khmAdOCVmVZgupibW95RZh6EJ-r7EWe1dXyMnbdOhavGVage5HNH3bANGYzzMEoxXXMXuxouGbEEA",
                "open_external_url_with_in_app_browser": true,
                "title": "",
                "url": "http://ang.execross.com"
            },
            {
                "icon_url": "",
                "image_url": "",
                "is_pinned": false,
                "is_verified": false,
                "link_id": "18010010174298412",
                "link_type": "external",
                "lynx_url": "https://l.instagram.com/?u=https%3A%2F%2Fexecross.com%2F%3Ffbclid%3DPAZXh0bgNhZW0CMTEAAaaEWh-n9ReSsIqbNT6YO-23vZVvyot79K6sbHqXDeI8OTApbBv1ojbEspg_aem_yiG1dg7yyoTo_Tvz6hl8FA&e=AT0s77TJDhtKkA7_Ahl6G1lnw6s4Tb6tE4LhuvW4J8WZUOLDTUzKLRBiLP1vhvVBXFETqgSQeO7-6G8rs_PEx5ViyDySrC0U43j70g",
                "open_external_url_with_in_app_browser": true,
                "title": "",
                "url": "https://execross.com"
            }
        ],
        "business": {
            "category": null,
            "contact": "",
            "status": false
        },
        "category": null,
        "categoryID": "",
        "email": "",
        "exclusief": false,
        "fanclub": {
            "fanclubId": null,
            "fanclubName": null,
            "subscriber": null
        },
        "follower": 5749,
        "following": 142,
        "fullname": "Asking Ang",
        "highlight": [
            {
                "count": "1",
                "cover": "https://instagram.fktm21-1.fna.fbcdn.net/v/t51.2885-15/438864464_443454604719365_7761716379937184298_n.jpg?stp=c0.247.640.640a_dst-jpg_e15_s150x150&_nc_ht=instagram.fktm21-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=cK8WE0PTGEEQ7kNvgEVyX0P&_nc_gid=81c2fa0202cf4cf883eaabd452e3fdd4&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_AYCB35y46HXuCKoAkSeYrQnJBT7wKPuUiX20cVs9xnqBjQ&oe=6705456A&_nc_sid=94fea1",
                "title": "Dhiyaa'",
                "url": "https://www.instagram.com/stories/highlights/17901626525970784/"
            },
            {
                "count": "2",
                "cover": "https://instagram.fktm21-1.fna.fbcdn.net/v/t51.2885-15/214366096_249624753304138_6970227549977833120_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fktm21-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=pkIBENiRFLUQ7kNvgHaxs4R&_nc_gid=81c2fa0202cf4cf883eaabd452e3fdd4&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_AYBYep2c0MSzBi1mbz3YqberxC4lw27n_qs7bfIrvwlHww&oe=67054B2F&_nc_sid=94fea1",
                "title": "Rhyme \u270d",
                "url": "https://www.instagram.com/stories/highlights/17858299709542615/"
            }
        ],
        "lastpost": [
            {
                "caption": "",
                "comment": "0",
                "created": "1 year ago",
                "like": "0",
                "page": "https://instagram.com/p/3167697185853139864/", 
                "url": "https://flufi-cdn.com/instagram/U2FsdGVkX1/6551YoDlBB9v0Q60nAXb2ERoLvR3Dp0ZZfnkestZzGP4ahIahZCySv7a/7w8q5mfzs1v0uwElDASZ9HhdD9b150KFnHMkjqpvuhD8qBZEB3DcGMWwO2jDyLZh/KE7Qf6bO5qfj4W8Uoo0ZtVpJRjNdNc9QjDrmNtXAayMqeq5a+iJaHKVfqTo5EBNyXVqQU6N2mz3h4LEr2dgpvv+D1jxKjreDdSvcizbH1rGqZQ8Z0X0/OfzwPNblw8jWtCg1vrlTuQiQ2YvdfpeMMfYJYQOqv+4xbhMHrM/xakhZ9DZbElSGDIzBYCZsFnLzAWbGKGwRJJ/uTyy/4pBT1Z6pCvZvNNTIAmho/dR3UAP1TWNGrw5yE2os8/6vLFxcBNTTBx+/Bz6CTVq/sLr9DGExd3IvnxZQZlat66A/75mVug6/dCfQq/a9uQsepd6mYTTl4ynwam8HDfN/KBNsvXGDMAGf68+S4r6SUwUP7MsQUOgK4viHuLTmiDwpSGId1/EknSMjm+DfFUltWDdSdfnmGwZKHBgAbzi52NWv3nxkXdvefmU/1ywnLJjNDfyLo4uTuM71oxBcF5g24wo7OuBfd8njsBlRyBuHetjergjxEk4HOnrbNdGHyi94EnIaacpPSCtxsBW2B4aFevmHH4dmKS5JRBo/0zmKd0nwI7bxx/ucIfRBbOZUu25s3a9lHu1O+TYrs7I8IQ6I0N+gldQiXDF2KcF1t3rqe4qUyEZ+ghm4NDa4RRWzzK9QuemSmLoPwy8u63ep+9+fgpFwPM4lIxt2EXXGEaWYCU3NENYFzvvIIJEDfRRV/AHcjAhJiKucMTAr5ntnnIQpOBiQek+pCQfAAPJbboh9SkMwISDMXXrqu+BsWnLeNOSBvrO3+XIsWEFUUrRByYBlfogrgPcZTK2ebtg3JOJmYU=",
                "video": false
            },
            {
                "caption": "",
                "comment": "0",
                "created": "1 year ago",
                "like": "0",
                "page": "https://instagram.com/p/3167695818342145139/", 
                "url": "https://flufi-cdn.com/instagram/U2FsdGVkX18fr4ldzA8FBNbMXNJ6w/iDQoAHpf7U6C5JrIRVUg4hyOYF4uGPr6OachIqHX1pqrX8FbmSkSjWNCdUGphm0moVoGIBcdhcQLfDvG5dBnIQpybU/IN+Oa6cq+12WA9IC80o6vE5cDMXohNtlFJsj1KxOiD+rxHvOS/1jiD4rSUTL05BY+taW7fqclA6zuoCDWGPl8AeTxL2QcQDLmRM1fyyV1e6fO272Z+oI//yhQdlXpt/LpRg9CcGiogFqPhnxSpN7jFSnquy92R8IrVFyEa0p/1CM7lXdAH0Hhl5JWqUJYJ+ARMn+dekf3LjsO/m5NQsQGzxbV2ueoSFxoIsZa8YZz1IYjLITyWsl8u05rWEArhr1xM8ABP+rEpARZfBizrSzwX4vUeLOfM9H51ayhw7+lAPdXz5OCril9e32+3tLnrcE2KeDQcRXa9J+FDMQZP/wy8FFBmjkx4SpHK0e4EifPssbDXVFfjvPQsb1/T1n+JTwouxBkS5A4LLPY2pC4n8a+nkbR4YYfqcjPvWm7/d9aDUl1gwgksUw/G7Y9z0MAsXfc2vQtL9MwMSWGzhL+unvRH7P/1IQT0U26b6ZjV+0tkKIJ/YBVFOlIjIZiv3Q/nIfH+l/tkN/gwLQHqxvWDOJ2lwV+sYmJl0K9/H4v7pyV2OiUTxi+YMtiI+1/Xq7COITDg7atse9yBxccC60wcLApQRz4x2QoSQkzJv5xK3BxFAkBucOZIwiNCmcorw0Lb+hLUZPfm/xCRg8bC7UatsjuxhiA7La6v+1z01Eia3yDy+KfnoZsL+jYV8fIDhO3Zq9SmpoCxBBlcwQxMFdNJNLqdTxdje8jFpcsZNBji5cYR2VvuZoUP+FtVBKNKlNVeIFkE/fvtzzwgwA2rjTFlk3eDdiRKhtLkt9YPyPAI4CuuJAzqlPgQ=",
                "video": false
            },
            {
                "caption": "SunSet",
                "comment": "0",
                "created": "1 year ago",
                "like": "0",
                "page": "https://instagram.com/p/3167695353361664810/", 
                "url": "https://flufi-cdn.com/instagram/U2FsdGVkX18uxTVrQ6rALPc74p2K3SgA/9rJgpRgQAPQMxoCCW0rJecap9Bg+GhQXDCzv85BnLEu5wY2pBfFuD4iwV+v0+VUKd9dkmHbNp7keEhxXqlkwB6CKPVm2nqepzmKu3+SgUDPRloB7dg/mmC3hqMMIa9l02LA0gRq08QEp4Hq9PyYh5KEq4M5XPL+AJfIXYgtI1jwE6fcGhp0c1OD2DrVNzgGcaB+RCDS5iwPuGBRXeRplTLRXQJK6NI1iOrtEzP488AmkweA4xRtWibXFzl0hDvjVXRCIq6OsqxjNtf2WsnYP7Z7DcQgzGof84CmC/hntRh4HMevUTPxPKfTg5+IfjTt25u6A031tX7E1WAuIASSA5bDOBpKkIAtFSgmucwXceMS3LSsZo83LdVRokoZzxmAQf3OqcWpsmpxkwwigolUA0S2UtaLwkGg7ZwZN3XM4VBAp3LJUmhfzVXRRo/eg5nEw/VMRhJBlc22B8iCup7FdEXX/rSJqnxfUjRyd3WTo1piKpDol1zWc2/Htxsm3uvNkWLz8cW2CJf/CZU89NqnftWBDAk5Rn0fXrgnCDOGd/H5kcxfqeQev/W/Y5QL6hifpTVwidutbyYjGGvdv7nnv3vqY6XF9WmyDJubsEATmCK65ZzwSj+/ByWeiLaAUbSQImi+OgyHAiQ7T+AZEV/AA0mssLVZ2saYtryIlFW/ojVY0yif8OO1PQ+HV5NpMJqI2Ptyr9lmi0p0+9cZ4gEF6Fz9wfGLPjIEGvjzL4fyjAU3NZQMR7P6skNCO/ThI/zUkiVYPoMYONy/17rXcUGqToqrXF4LtLRot5JG8NReVAERPSN/5DSJIE2w8d/Gw2aoMnEWJj/VSoFMJatvrjd/PJCFOUyX+C32jLYJX5oJDjkVj+fKKMv+4dNnOWHYbUwrUXgBcQTJNxo=",
                "video": false
            },
            {
                "caption": "#Bird",
                "comment": "0",
                "created": "1 year ago",
                "like": "0",
                "page": "https://instagram.com/p/3167692770140016835/", 
                "url": "https://flufi-cdn.com/instagram/U2FsdGVkX183MERdAz0D2y6WF1jb+AQ4du23nMCyIyQwGekDGI9q1PQTCEov+BqRse1MOBdNMdfdJxKalCpOcNprim7B4yVbeUOVDIPZcDeFJYjW634AaupktCaY4YzebMBY88yE6W3LJ2GJdpuR/jYd3dnrV0nM13rhasqzmd7NdUF7aFXyI6bEFLXInVRlFpSiWVSIY8sHoXEgLMmC7U8DVh3OE86JdyFJWAyYWYoWU4smOSv46V9PARGjni23d+ZoCr8VwoMj/0b9lk0v7CXhhpvgc3CWrkcrQVL5+jD1rsiTk730iIS1QRhpkj/VEB7x8VNZwJh6OiSeK9UWLw/+hGzwetcFHIzramrSOYlrET+uQmhkYrpZrz6a9I0b9DsiI3xBWHuwgimRfzhIIMcvjteJAKviiyEzYVj3uxxGlf0/t4er44dO6FbajTAkO2VWSu9oSBsyqRx12VGG7e3t4izVEtHIuFpbheXCaJiJ+y0s5sGvOHnIle4V5cbpRC1GTDZwpnQ7Qhcj//tzkU4ocRbwKFcI9vKP8G0pUvzi7Oem/xlJszw1zX3Huaj7cxXAZh3Su36foEudu1tfs2jElhU1rl34IjeBTSCM29095j29xCSmB14gcQNbdnooH+Dw+SiATFZcsR0Eg//7wYV+14mKGO9ka2sD3uQCgBd05j71NWWUCLqj73G7pn9KQjkew/LHKBUXB6vchJD4KYub4brFjSCvLfSPe1wZxTb4WNmZnxKIJfchd5+KPB9lTve3m5E0mSIkbkA7Fp8uTihfMR8gY+5MoJ7cs5Sz9QMbK3OJZOXqXECLiL+62mxHqLb+T3zoFTCu1J5H4qZ4ba6THr0w7Q6t3Y8larUaSSHViOn2SnwuvONeNsSf+pzFkz7SRDtGcSF1rqFpGOqeU+XVcA6TOhhUbxCHXopZI3E=",
                "video": false
            },
            {
                "caption": "Hmm",
                "comment": "0",
                "created": "3 years ago",
                "like": "0",
                "page": "https://instagram.com/p/2529319547288491459/", 
                "url": "https://flufi-cdn.com/instagram/U2FsdGVkX18N2gzrjx0aw7npgurTlljCVhzyTJT/NG3n+UuM49vLMtfyL1V4z8+1Kr4JQYwzwgBfT035tK+ZZI67+pS0iGGFZUwYQnSk7tvxL1yzn16JtbH2ltbPjMvP8UNwSlDLv/zaiSrz9dKOkLztKHn0ErSDyMKAWpqJ0hR8ZEwXaslSqY1i+GVjhAG9ZMSZidtqNLQrGIRXWhaYxkIn8n8jGgh3bpZhp2oc/K3ORECYyGSpcPkZHHJvOevu6xO1WdKCxIxpSQ9pAoo/0hLrpgiYg7MURiUGocVcQuO6Kvl4EdJEndM6mIY6uZNgaIyqoQvJwSaXZl+hTwDI3ycq8FnVggtFpGHuB7ozrj7vkjPGUjteZIo4Aqj9BS1vqxDMOIp89p1/dJOvPg2MjehpXl5EsbzSAKY+lNXUXBsyAcryJpXsKQa/W6DvpN7NE+wvZVDQ7uUP1IMGyC1JVN/ziLrgeswSzdufpdcVs5MnC7LUcFlGkpe3cHzrjuXlU/ddULXZaGwD65zq6WjiiYGywU087z9W7tUHADBiPGyClerCDeAZWhtkkzjJxCgJYi3PfTRNbxYeyB712TH6AghLPD215StCfCsEpoNp/WoukWCmvHgGIvAWNko1j2qcqwei7swjXV+6xrLuNppMX6MhdScBBEVyYybZ8a5apFP5I/zkR3EJZQ+5mg7RkOC4h+3Z+f3I52Ffp2e27Er0aaeASdSCFxNczcufFX8mDns+bY0nJE/moEyUV3ei+M1XngQuzR7qh+oflDjsjqBfVJ9KhbzSF7a/YbWAgcEKFkLsw+N+bl6yJ9J6HWKGw1tny4Nk/kKrB7D1/PBD1LHXe2XC07N8NqCjkOsZXkIE7H0tIOPq0z7+D1CTWyCH7npPTU1uma3ZIIThxykFOE16mT7zIxij2dA+CjoDesN/Xzw=",
                "video": false
            },
            {
                "caption": "Unless you don't realize your mistake, you haven't done it.\nJust like error of code that teaches us something we didn't know before.\n\nFull Documentation: https://api.imjustgood.com\n\n #apimedia  #apiinstagram  #imjustgood",
                "comment": "0",
                "created": "3 years ago",
                "like": "0",
                "page": "https://instagram.com/p/2521397771152493432/", 
                "url": "https://flufi-cdn.com/instagram/U2FsdGVkX1/cFtC2Xr7NIf2vV9oGmu14FIHOrI37gWISAerWQivOtMOW84FuET0e6YCWD6OWlvJj+UujC8rKU+EL4Yw6OdAJ01Zkurrex/rDgKj0ADGUA7QwQimi+xarA4H/pA9TQ3SMCrJXepfBwTAAcpWaEj3G01fV2jGUajq4gCP0QyKAjTtUbLtzn4VFG/PuZR2VxRujpK7RNxetlStv8cUsR0r/FIQo5JY1grC9iSwSTUosr+B3MDFeYbEBTBvm4ZrAumaHXCF/evqBqsimdgJnmgUNl1u4AKeb44V6fvBNkjvJRuCCa4wNqsyg9xjyJofELtJG2lxdf1qMhUXWr0yLKs8UG5RIJIBpwjYAZPYAulXOUx8vbGnZzMlrfg+G8zpt4Q+64FDKrY7ldf8gKK/84ZDSkugkC/F6J37+bnKi3hfVs/sI/ELsQt2v2lX1yuR2xegcyRo0N4g+gzJrJzrRpo0vj90x5lFZJoWcSNiCDQNc0JqLs2nUqwgJthHAe8tb9Dh3BPFOjRy9Q3F21/0KBYp6dLZ4BcC/3T9/Jn/oLAJLJMzOkmlf1haEZSIpl7LAlmNG6WazqGn5ew65xUoe7b/mSimMLhh0Tay7jjQ659lw3nfxxA/0IILVi4fHoR3MmvBqaY/+KqiPSE+wLdm98d11tznyBIQWF3f7VveLgH3ZiP6asMl7+78XaOXN6Yujpem0uC6NftKIcXeMXapyeVZRjgR42oBP3nIUvr4f3SXLiy29o40TNnyQR/RF+pMzCj4Em4C++ANTtuV9wLXUQqiycGVykr6Dyl2RbkxESNR/H6WPQEINcKK4RbJkwaNrHUbPJCPQ2V0VeOerg1Ca2ceHCTOzT2NTYjhbZOFXO0GxngNUsjtDYPRHzV5BjJCfb162uZE/PZdWZUSAyFmzY+LM2ZBDVDls7p4=",
                "video": false
            }
        ],
        "lastreels": 0,
        "phone": "",
        "picture": "https://scontent-gmp1-1.cdninstagram.com/v/t51.2885-19/448054598_2717759565065970_3110878031122831592_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=106&_nc_ohc=KRhulgI3F18Q7kNvgHrkMR_&_nc_gid=307a8ff321d74dd48f83fd8038b3825e&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AYBYkEP0LM5KyWK2PCllP3xosuNaKk6ruf2an_4wnNF6ng&oe=67054746&_nc_sid=1e20d2",
        "post": "7",
        "private": false,
        "profile": "https://instagram.com/this.ang",
        "storie": [],
        "threadsUrl": "https://www.threads.net/@this.ang?modal=true&xmt=AQGzu8rxnJrw0AsTvEyjkprV7JSkI2YVottQO-VCEqKIlCI",
        "type": 1,
        "username": "this.ang",
        "verified": false,
        "whatsappLinked": false
    },
    "status": 200
}

"""
