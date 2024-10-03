import requests
import random

class ExecrossAPI:
    def __init__(self, base_url, apikey):
        self.base_url = base_url
        self.apikey = apikey
        self.session = requests.Session()
        self.session.headers.update({'apikey': self.apikey, 'Content-Type': 'application/json'})

    def getProxies(self):
        endpoint = f'{self.base_url}/proxies'
        response = self.session.get(endpoint).json()
        if response and response['status'] == 200:
            proxies = response['result']['proxies']
            return random.choice(proxies).split(':')[0]
        return None

    def getQR(self, params):
        url = f'{self.base_url}/loginqr'
        url2 = f'{self.base_url}/reqpin'
        url3 = f'{self.base_url}/reqtoken'
        response = self.session.get(url, params=params).json()
        print(response)
        if response and response['status'] == 200:
            params2 = {
                'apikey': self.apikey,
                'session': response['result']['session']
            }
            response2 = self.session.get(url2, params=params2).json()
            if response2 and 'authToken' in response2['result']:
                return response2
            else:
                print(response2)
                response3 = self.session.get(url3, params=params2).json()
                return response3
        else:
            print(f"Error: {response.get('error', 'Unknown error')}")

    def getQRV1(self, params):
        url = f'{self.base_url}/loginqrv1'
        url2 = f'{self.base_url}/reqpinv1'
        url3 = f'{self.base_url}/reqtokenv1'
        response = self.session.get(url, params=params).json()
        print(response)
        if response['status'] == 200:
            params2 = {
                'apikey': self.apikey,
                'session': response['result']['session']
            }
            response2 = self.session.get(url2, params=params2).json()
            if 'authToken' in response2['result']:
                return response2
            else:
                print(response2)
                response3 = self.session.get(url3, params=params2).json()
                return response3
        else:
            print(f"Error: {response.get('error', 'Unknown error')}")

    def getEmail(self, params):
        url = f'{self.base_url}/loginemail'
        url2 = f'{self.base_url}/reqemailtoken'
        response = self.session.get(url, params=params).json()
        print(response)
        if "pincode" in response['result']:
            params2 = {
                'apikey': self.apikey,
            }
            response2 = self.session.get(url2, params=params2).json()
            return response2

    def getEmailV1(self, params):
        url = f'{self.base_url}/loginemailv1'
        url2 = f'{self.base_url}/reqemailtokenv1'
        response = self.session.get(url, params=params).json()
        print(response)
        if "pincode" in response['result']:
            params2 = {
                'apikey': self.apikey,
            }
            response2 = self.session.get(url2, params=params2).json()
            return response2

    def exampleAddFriendPrimary(self, params):
        url = f'{self.base_url}/addfriend'
        response = self.session.get(url, params=params).json()
        return response

    def exampleAddFriendSecondary(self, params):
        url = f'{self.base_url}/addfriend'
        response = self.session.get(url, params=params).json()
        return response

    def refreshToken(self, params):
        url = f'{self.base_url}/refreshtoken'
        response = self.session.get(url, params=params).json()
        return response

    def lineAppname(self):
        url = f'{self.base_url}/appnames'
        response = self.session.get(url).json()
        if response['status'] == 200:
           return response['result']['appNames']

    def getStory(self, params):
        url = f'{self.base_url}/linestory'
        response = self.session.get(url, params=params).json()
        return response

    def getPost(self, params):
        url = f'{self.base_url}/linepost'
        response = self.session.get(url, params=params).json()
        return response 

    def friendRecomendation(self, params):
        url = f'{self.base_url}/friendrecomendation'
        response = self.session.get(url, params=params).json()
        return response

    def messageIdToURL(self, params):
        url = f'{self.base_url}/msgidtourl'
        response = self.session.get(url, params=params).json()
        return response

    def convertParseUrlToExtension(self, params):
        url = f'{self.base_url}/convertparseurl'
        response = self.session.get(url, params=params).json()
        return response

    def webp2mp4(self, params):
        url = f'{self.base_url}/webp2mp4'
        response = self.session.get(url, params=params).json()
        return response

    def mp42gif(self, params):
        url = f'{self.base_url}/mp42gif'
        response = self.session.get(url, params=params).json()
        return response

    def vid2Apng(self, params):
        url = f'{self.base_url}/video2apng'
        response = self.session.get(url, params=params).json()
        return response

    def smulePost(self, params):
        url = f'{self.base_url}/smuledl'
        response = requests.get(url, params=params).json()
        return response

    def smuleProfile(self, params):
        url = f'{self.base_url}/smuleprofile'
        response = requests.get(url, params=params).json()
        return response

    def instagramPost(self, params):
        url = f'{self.base_url}/instapost'
        response = self.session.get(url, params=params).json()
        return response

    def instagramStory(self, params):
        url = f'{self.base_url}/instastory'
        response = self.session.get(url, params=params).json()
        return response

    def instaStalker(self,params):
        url = f'{self.base_url}/instastalker'
        response = self.session.get(url, params=params).json()
        return response

    def instagramProfileDetails(self,params):
        url = f"{self.base_url}/instaprofile"
        response = self.session.get(url, params=params).json()
        return response

    def downloadXpost(self,params): #Twitter
        url = f'{self.base_url}/twitterdl'
        response = self.session.get(url, params=params).json()
        return response

    def tweetProfile(self, params):
        url = f'{self.base_url}/tweetprofile'
        response = requests.get(url, params=params).json()
        return response

    def downloadFacebook(self,params):
        url = f'{self.base_url}/facebookdl'
        response = self.session.get(url, params=params).json()
        return response

    def downloadTiktok(self,params):
        url = f'{self.base_url}/tiktokdl'
        response = self.session.get(url, params=params).json()
        return response

    def tiktokProfile(self,params):
        url = f'{self.base_url}/tiktok'
        response = self.session.get(url, params=params).json()
        return response

    def combineImages(self,filenamed, files, data):
        url = f'{self.base_url}/combine'
        headers= {"apikey": self.apikey}
        response = requests.post(url, headers=headers, files=files, data={'urls': data['urls']})
        if response.status_code == 200:
            with open(f'{filenamed}', 'wb') as f:
                f.write(response.content)
            return f"Image successfully saved to: {filenamed}"
        else:
            return f"Failed to save image. Status code: {response.status_code}, Response: {response.text}"

    def faceSwap(self, files=None,params=None):
        url = f'{self.base_url}/swapface'
        headers= {"apikey": self.apikey}
        response = requests.post(url, files=files, params=params, headers=headers)
        return response.json()

    def youtubedl(self,params):
        url = f'{self.base_url}/youtubedl'
        response = self.session.get(url, params=params).json()
        return response

    def youtubeQuery(self,params):
        url = f'{self.base_url}/youtubequery'
        response = self.session.get(url, params=params).json()
        return response

    def youtubeTrendingVideo(self,params):
        url = f'{self.base_url}/ytvideotrend'
        response = self.session.get(url, params=params).json()
        return response

    def youtubeTrendingMusic(self,params):
        url = f'{self.base_url}/ytmusictrend'
        response = self.session.get(url, params=params).json()
        return response

    def fancy(self,params):
        url = f'{self.base_url}/fancy'
        response = self.session.get(url, params=params).json()
        return response

    def github(self,params):
        url = f'{self.base_url}/github'
        response = self.session.get(url, params=params).json()
        return response

    def githubClone(self,params):
        url = f'{self.base_url}/githubdl'
        headers = {
            "apikey": self.apikey
        }
        response = requests.post(url, json=params,headers=headers).json()
        return response