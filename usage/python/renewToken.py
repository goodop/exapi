import requests
from datetime import datetime, timedelta
import json

base_url = 'https://execross.com/api/v3'

def getAppname():
    endpoint = f'{base_url}/appnames'
    headers = {
           "apikey": 'forexecman'
    }
    response = requests.get(endpoint,headers=headers).json()
    if response['status'] == 200:
        return response['result']['appNames']

def refresh(authToken,refreshToken):
    appname = getAppname()['windows'] # Appname must desktopwin or desktopmac.
    headers = {
             "apikey": 'forexecman'
    }
    params = {
        'appName': appname,
        'authToken': authToken,
        'refreshToken': refreshToken
    }
    response = requests.get(base_url + '/refreshtoken', params=params,headers=headers).json()
    if response['status'] == 200:
       return response['result']['newToken']
    return response['message']

def renewToken(authToken, refreshToken, fortomorrow=False):
  try:
      headers = {
             "apikey": 'forexecman'
      }
      checkExpired = requests.get(f'{base_url}/tokenexp?authToken={authToken}',headers=headers).json()
      if checkExpired['status'] == 200:
         dtime = datetime.fromtimestamp(int(checkExpired['result']['insecs']))
         now = datetime.now()
         today = datetime(now.year, now.month, now.day)
         tomorrow = today + timedelta(days=1)
         after_tomorrow = tomorrow + timedelta(days=1)
         istomorrow = tomorrow <= dtime < after_tomorrow
         isexpired = dtime < now
         if fortomorrow:
            if istomorrow:
               data = refresh(authToken,refreshToken) # refresh waiting if token will expired tommorow
               response = {
                  "status": True,
                  "token": data
               }
               return response
            return "The authToken Expired is not tommorow"
         else:
            if isexpired:
               return 'Token already expired'
            else:
               data = refresh(authToken,refreshToken) # Refresh with no waiting expired 
               response = {
                  "status": True,
                  "token": data
               }
               return response
  except Exception as e:
        print(e)

refr = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2NTFkMzgwOS0yYmU1LTQ1YTEtYTFiMy04NWUyZGJmMjQwMzAiLCJhdGkiOiIwNjcwM2U0YS0wYzdjLTRkYTctOGEzMy01NTJlODhjNjMwNzgiLCJhdWQiOiJMSU5FIiwicm90IjoiU1RBVElDIiwiaWF0IjoxNzI1MzMxMDU2LCJleHAiOjE3NTY4NjcwNTYsInNjcCI6IkxJTkVfQ09SRSIsInZlciI6IjMuMCIsImFpZCI6InUxMmU4ZGY0YTZlNmM3MmVmNjJmZjdiODM4NmJkMzA1MiIsImxzaWQiOiI0MDkxNTA3OS1kOTRkLTQwNTYtYThkMi02ZDk1NmFkZDg5MzUiLCJkaWQiOiJOT05FIiwiYXBwSWQiOiIwMTAwMDAwMDAwIn0.V9gfKsPvrF7rlpHQlI4nwzdw3DOBmO94qsWDIxzst4g'
auth = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwNjcwM2U0YS0wYzdjLTRkYTctOGEzMy01NTJlODhjNjMwNzgiLCJhdWQiOiJMSU5FIiwiaWF0IjoxNzI1MzMxMDU2LCJleHAiOjE3MjU5MzU4NTYsInNjcCI6IkxJTkVfQ09SRSIsInJ0aWQiOiI2NTFkMzgwOS0yYmU1LTQ1YTEtYTFiMy04NWUyZGJmMjQwMzAiLCJyZXhwIjoxNzU2ODY3MDU2LCJ2ZXIiOiIzLjAiLCJhaWQiOiJ1MTJlOGRmNGE2ZTZjNzJlZjYyZmY3YjgzODZiZDMwNTIiLCJsc2lkIjoiNDA5MTUwNzktZDk0ZC00MDU2LWE4ZDItNmQ5NTZhZGQ4OTM1IiwiZGlkIjoiTk9ORSIsImN0eXBlIjoiREVTS1RPUF9NQUMiLCJjbW9kZSI6IlNFQ09OREFSWSIsImNpZCI6IjAxMDAwMDAwMDAifQ.JJf71nO_cNCHSj27Gr1TDXM4Jq-eFjX0SoSdPJK63PA'
data = renewToken(auth, refr, fortomorrow=False)
if data['status']:
   print('New Token:',data['token'])
   # save the token on your data for login.
else:
   print(data)


# Example use in line login
refr = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2NTFkMzgwOS0yYmU1LTQ1YTEtYTFiMy04NWUyZGJmMjQwMzAiLCJhdGkiOiIwNjcwM2U0YS0wYzdjLTRkYTctOGEzMy01NTJlODhjNjMwNzgiLCJhdWQiOiJMSU5FIiwicm90IjoiU1RBVElDIiwiaWF0IjoxNzI1MzMxMDU2LCJleHAiOjE3NTY4NjcwNTYsInNjcCI6IkxJTkVfQ09SRSIsInZlciI6IjMuMCIsImFpZCI6InUxMmU4ZGY0YTZlNmM3MmVmNjJmZjdiODM4NmJkMzA1MiIsImxzaWQiOiI0MDkxNTA3OS1kOTRkLTQwNTYtYThkMi02ZDk1NmFkZDg5MzUiLCJkaWQiOiJOT05FIiwiYXBwSWQiOiIwMTAwMDAwMDAwIn0.V9gfKsPvrF7rlpHQlI4nwzdw3DOBmO94qsWDIxzst4g'
auth = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwNjcwM2U0YS0wYzdjLTRkYTctOGEzMy01NTJlODhjNjMwNzgiLCJhdWQiOiJMSU5FIiwiaWF0IjoxNzI1MzMxMDU2LCJleHAiOjE3MjU5MzU4NTYsInNjcCI6IkxJTkVfQ09SRSIsInJ0aWQiOiI2NTFkMzgwOS0yYmU1LTQ1YTEtYTFiMy04NWUyZGJmMjQwMzAiLCJyZXhwIjoxNzU2ODY3MDU2LCJ2ZXIiOiIzLjAiLCJhaWQiOiJ1MTJlOGRmNGE2ZTZjNzJlZjYyZmY3YjgzODZiZDMwNTIiLCJsc2lkIjoiNDA5MTUwNzktZDk0ZC00MDU2LWE4ZDItNmQ5NTZhZGQ4OTM1IiwiZGlkIjoiTk9ORSIsImN0eXBlIjoiREVTS1RPUF9NQUMiLCJjbW9kZSI6IlNFQ09OREFSWSIsImNpZCI6IjAxMDAwMDAwMDAifQ.JJf71nO_cNCHSj27Gr1TDXM4Jq-eFjX0SoSdPJK63PA'
new = None
data = renewToken(auth, refr, fortomorrow=True) # refresh when tomorroe expired.
if data['status']:
    client = LINE(idOrAuthToken=data['token'])
    new = data['token']
else:
    if not new:
       client = LINE(idOrAuthToken=auth)
    else:
       client = LINE(idOrAuthToken=new)  