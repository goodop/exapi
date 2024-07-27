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

    def smuledl(self, params):
        url = f'{self.base_url}/smuledl'
        response = self.session.get(url, params=params).json()
        return response

    def instagramPost(self, params):
        url = f'{self.base_url}/instapost'
        response = self.session.get(url, params=params).json()
        return response

    def instagramStory(self, params):
        url = f'{self.base_url}/instastory'
        response = self.session.get(url, params=params).json()
        return response
