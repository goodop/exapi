import requests
import json

endpoint = 'https://execross.com/api/v3/spotilist'
headers = {
    'apikey': 'forexecman'
}
params = {
    'query': 'mungkin-nanti'
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
    "result": [
        {
            "album_name": "Bintang Di Surga",
            "artist": "Peterpan",
            "duration": "4:28",
            "mp3Preview": null,
            "number": 1,
            "title": "Mungkin Nanti - From \"Alexandria\" Soundtrack",        
            "url": "https://open.spotify.com/track/3IZduSshBfpO2qZGCusLsg"    
        },
        {
            "album_name": "The Journey Vol. 1",
            "artist": "Peterpan",
            "duration": "4:29",
            "mp3Preview": "https://p.scdn.co/mp3-preview/852e5451882901a676b08015c08aeb9766d1a1b8?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 2,
            "title": "Mungkin Nanti",
            "url": "https://open.spotify.com/track/2KqMb5rJHmfGDFAZPj05AJ"    
        },
        {
            "album_name": "Bintang di Surga",
            "artist": "Noah",
            "duration": "4:29",
            "mp3Preview": null,
            "number": 3,
            "title": "Mungkin Nanti",
            "url": "https://open.spotify.com/track/4j4F6vkb8niNvoXA7MPP2d"    
        },
        {
            "album_name": "Sebuah Nama, Sebuah Cerita",
            "artist": "Peterpan",
            "duration": "4:29",
            "mp3Preview": null,
            "number": 4,
            "title": "Mungkin Nanti",
            "url": "https://open.spotify.com/track/6iVMdJy1PpnbouyKkfnn57"    
        },
        {
            "album_name": "Mungkin Nanti (Acoustic)",
            "artist": "Mr. Ali, Hilman dr",
            "duration": "5:04",
            "mp3Preview": "https://p.scdn.co/mp3-preview/a7955f3b0b3b8a09f285282e1a6b07b7dc8b86e0?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 5,
            "title": "Mungkin Nanti - Acoustic",
            "url": "https://open.spotify.com/track/01FzwiGZIbZbnXr99wP80S"    
        },
        {
            "album_name": "Maafkan Aku",
            "artist": "Jerome Clement",
            "duration": "5:15",
            "mp3Preview": "https://p.scdn.co/mp3-preview/8974946fd851808912d0e981110228966c02427e?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 6,
            "title": "Mungkin Tidak",
            "url": "https://open.spotify.com/track/0IJ1oev9dY0JRVxtU8IRKZ"    
        },
        {
            "album_name": "Mungkin Nanti",
            "artist": "Felix Irwan",
            "duration": "4:45",
            "mp3Preview": "https://p.scdn.co/mp3-preview/b38389ea2963af78f9779e25d8b01a12b7c24881?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 7,
            "title": "Mungkin Nanti",
            "url": "https://open.spotify.com/track/0n2M2oAOkZLUEdVIcycr6L"    
        },
        {
            "album_name": "Mungkin Nanti (Reimagined)",
            "artist": "Mitchell Zia",
            "duration": "3:19",
            "mp3Preview": "https://p.scdn.co/mp3-preview/dfc9712cbe341a8cb030d1a7544ca6e2fa3994b4?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 8,
            "title": "Mungkin Nanti - Reimagined",
            "url": "https://open.spotify.com/track/6Ru6K73RsW1k9oL1NQbBvH"    
        },
        {
            "album_name": "Selamat Datang di Ujung Dunia",
            "artist": "Lomba Sihir",
            "duration": "3:09",
            "mp3Preview": "https://p.scdn.co/mp3-preview/526ff11127286801d31ed8bfb485fd6004ea15bc?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 9,
            "title": "Mungkin Takut Perubahan",
            "url": "https://open.spotify.com/track/5431aNwjj7msmgVrCwgEcq"    
        },
        {
            "album_name": "Alexandria (From \"Alexandria\" / Original Motion Picture Soundtrack)",
            "artist": "Peterpan",
            "duration": "5:25",
            "mp3Preview": null,
            "number": 10,
            "title": "Mungkin Nanti",
            "url": "https://open.spotify.com/track/5DR141x38j4fc8ntOMS1zV"    
        },
        {
            "album_name": "Apa Mungkin",
            "artist": "Bernadya",
            "duration": "3:59",
            "mp3Preview": null,
            "number": 11,
            "title": "Apa Mungkin",
            "url": "https://open.spotify.com/track/5KYUrBgdbIcqwaGSIgfXPl"    
        },
        {
            "album_name": "lelah",
            "artist": "Maybemey",
            "duration": "3:22",
            "mp3Preview": "https://p.scdn.co/mp3-preview/b8419384610b633d5c9cf7b8ea40bd6741475877?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 12,
            "title": "lelah",
            "url": "https://open.spotify.com/track/0BVhyQVwyod32fcqKA4T8l"    
        },
        {
            "album_name": "And the story begins",
            "artist": "Anneth",
            "duration": "3:51",
            "mp3Preview": "https://p.scdn.co/mp3-preview/c488ab9158702031a69ccf2d753958ed5a59a079?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 13,
            "title": "Mungkin Hari Ini Esok Atau Nanti",
            "url": "https://open.spotify.com/track/2ULbjOlhOCLjKLDalQ32xN"    
        },
        {
            "album_name": "Vol 2",
            "artist": "Matamusik",
            "duration": "5:10",
            "mp3Preview": "https://p.scdn.co/mp3-preview/7c41d54b1089fa8b552518a5c96357eddff13918?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 14,
            "title": "Mungkin Nanti - Remastered",
            "url": "https://open.spotify.com/track/6FFgeM2nz3MACqxf2moCCo"    
        },
        {
            "album_name": "Mungkin Hari Ini Esok Atau Nanti",
            "artist": "Anneth",
            "duration": "3:51",
            "mp3Preview": "https://p.scdn.co/mp3-preview/c488ab9158702031a69ccf2d753958ed5a59a079?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 15,
            "title": "Mungkin Hari Ini Esok Atau Nanti",
            "url": "https://open.spotify.com/track/7n5nvulc1oW1ErpeTrNezI"    
        },
        {
            "album_name": "Mungkin Nanti",
            "artist": "Mario G klau",
            "duration": "6:03",
            "mp3Preview": "https://p.scdn.co/mp3-preview/a145308526b8733c6e3aa8630b6a176007bf9565?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 16,
            "title": "Mungkin Nanti",
            "url": "https://open.spotify.com/track/7pb854JFHnq4n93smuYa12"    
        },
        {
            "album_name": "Mungkin Aku Tak Penting? (feat. Tish Errda)",      
            "artist": "Luqman Podolski, Tish Errda",
            "duration": "3:08",
            "mp3Preview": "https://p.scdn.co/mp3-preview/e4e8ed0457e48b382662618728f25046d1c4b11d?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 17,
            "title": "Mungkin Aku Tak Penting? (feat. Tish Errda)",
            "url": "https://open.spotify.com/track/3SSe3pzhdtPrVN0AqzUkx0"    
        },
        {
            "album_name": "Mungkin Nanti",
            "artist": "Remember Entertainment",
            "duration": "4:23",
            "mp3Preview": "https://p.scdn.co/mp3-preview/6501343e7081418b723f3dd1212408b40db335b8?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 18,
            "title": "Mungkin Nanti",
            "url": "https://open.spotify.com/track/03FmKds2U6keezmORBNCfd"    
        },
        {
            "album_name": "Mungkin Nanti",
            "artist": "Sasa Tasia",
            "duration": "4:23",
            "mp3Preview": "https://p.scdn.co/mp3-preview/ca60d4841b5855e4afab3985bb9cc22be25c662b?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 19,
            "title": "Mungkin Nanti",
            "url": "https://open.spotify.com/track/5Nd3jCTtxPfeXTfBqbufkE"    
        },
        {
            "album_name": "Mimpi",
            "artist": "Maybemey",
            "duration": "3:58",
            "mp3Preview": "https://p.scdn.co/mp3-preview/540e05e6a92fe50742374dd60bf7fc5e57895943?cid=8f777f61f80e4051b754d8e50310ad6e",
            "number": 20,
            "title": "Mimpi",
            "url": "https://open.spotify.com/track/6xV8ZcLWixQnFtYVCcd5YE"    
        }
    ],
    "status": 200
}


'''