from exapi import ExecrossAPI
api = ExecrossAPI(base_url='https://execross.com/api/v3', apikey='forexecman')

# Example 1: Getting QR Code
print("Example 1: Getting QR Code")
proxy = api.getProxies()
params_getqr = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'certificate': '',
    'proxy': proxy,
}
data = api.getQR(params_getqr)
print(data)

# Example 2: Getting QR V1
print("\nExample 2: Getting QR V1")
params_getqrv1 = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'certificate': '',
    'proxy': proxy,
}
data = api.getQRV1(params_getqrv1)
print(data)

# Example 3: Getting Email
print("\nExample 3: Getting Email")
params_getemail = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'certificate': '',
    'email': '',
    'password': '',
    'proxy': None,
}
data = api.getEmail(params_getemail)
print(data)

# Example 4: Getting Email V1
print("\nExample 4: Getting Email V1")
params_getemailv1 = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'certificate': '',
    'email': '',
    'password': '',
    'proxy': None,
}
data = api.getEmailV1(params_getemailv1)
print(data)

# Example 5: Adding Line Friend With Primary
print("\nExample 5: Adding Friend Primary")
params_addfriendprimary = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "uc23h7f331c8819j90fa9182db42a6e26:aWF0OiAbmkjDI5OTM2MTU2MDAK....",  # change with your primary token
    'proxy': None,
    'mid': 'ufed869bc1105aedd331665d57cea407d',  # mid target
}
data = api.exampleAddFriendPrimary(params_addfriendprimary)
print(data)

# Example 6: Adding Line Friend With Secondary
print("\nExample 6: Adding Friend Secondary")
params_addfriendsecondary = {
    'apikey': api.apikey,
    'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7',
    'authToken': 'FG4wDOtTGT0O6uoJoHE2.eUJFsM5SCU9I+3UdHR0WuG.....',  # change with authtoken v1 or v3
    'proxy': None,
    'mid': 'ufed869bc1105aedd331665d57cea407d',  # mid target
}
data = api.exampleAddFriendSecondary(params_addfriendsecondary)
print(data)

# Example 7: Getting Story Line
print("\nExample 7: Getting Story")
params_getstory = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': 'udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....',  # change with authtoken v1 or v3
    'proxy': None,
    'mid': 'ufed869bc1105aedd331665d57cea407d'
}
data = api.getStory(params_getstory)
print(data)

# Example 8: Getting Post Line
print("\nExample 8: Getting Post")
urlp = 'https://line.me/R/home/post?userMid=ufed869bc1105aedd331665d57cea407d&postId=1172180403371226572'
params_getpost = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....",
    'proxy': None,
    'mid': urlp[36:69],
    'postId': urlp.split("postId=")[1]
}
data = api.getPost(params_getpost)
print(data)

# Example 9: Line Friend Recommendation
print("\nExample 9: Friend Recommendation")
params_friendrecommendation = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....",  # change with your primary token or secondary token
    'proxy': None,
}
data = api.friendRecomendation(params_friendrecommendation)
print(data)

# Example 10: Line Image Message ID to URL
print("\nExample 10: Message ID to URL")
params_messageidtourl = {
    'apikey': api.apikey,
    'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
    'authToken': "udd56d5cd664be5ecf20d47238b3a8a3d:aWF0OiAxMDI5OTM2NTkxMDAK....",  # change with your primary token or secondary token
    'proxy': None,
    'messageId': "518437336376934529" # ID for images
}
data = api.messageIdToURL(params_messageidtourl)
print(data)

# Example 11: Convert Parse URL to Image Extension (.jpg)
print("\nExample 11: Convert Parse URL to Extension")
params_convertparseurl = {
    'apikey': api.apikey,
    'parseURL': "https://obs-us.line-apps.com/myhome/h/download.nhn?oid=d4905e97265d26bd395e157ccaf63621248b311t13dccbea"
}
data = api.convertParseUrlToExtension(params_convertparseurl)
print(data)
