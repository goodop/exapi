import requests,json

endpoint = 'https://execross.com/api/v3/ytvideotrend'
headers = {
    'apikey': 'forexecman'
}
params = {
    "region" : "ID",
    "countResult": 15 , # max 25, default 10
}
responsed = requests.get(endpoint,params=params, headers=headers).json()
print(json.dumps(responsed,indent=4))


"""
Result will be:
{
    "creator": "EXECROSS",
    "ip": "182.1.91.138",
    "result": [
        {
            "channelTitle": "Podkesmas",
            "likeCount": "8328",
            "thumbnailUrl": "https://i.ytimg.com/vi/t0uqcNl67sU/hqdefault.jpg",
            "title": "SHOWKESMAS - KALI INI KAMI DIBIKIN SKAKMAT INDY BARENDS",
            "url": "https://www.youtube.com/watch?v=t0uqcNl67sU",
            "videoId": "t0uqcNl67sU",
            "viewCount": "242554"
        },
        {
            "channelTitle": "AC Milan",
            "likeCount": "10537",
            "thumbnailUrl": "https://i.ytimg.com/vi/hw9IfSLr92U/hqdefault.jpg",
            "title": "Saelemaekers-Jovi\u0107-Reijnders for the Trofeo Silvio Berlusconi | AC Milan 3-1 Monza | Highlights",
            "url": "https://www.youtube.com/watch?v=hw9IfSLr92U",
            "videoId": "hw9IfSLr92U",
            "viewCount": "254774"
        },
        {
            "channelTitle": "Dhot Design",
            "likeCount": "124731",
            "thumbnailUrl": "https://i.ytimg.com/vi/QuQQTE8gVwc/hqdefault.jpg",
            "title": "LOMBA PART 2 (SPESIAL AGUSTUS) - Animasi Sekolah",
            "url": "https://www.youtube.com/watch?v=QuQQTE8gVwc",
            "videoId": "QuQQTE8gVwc",
            "viewCount": "2340185"
        },
        {
            "channelTitle": "Ewing HD",
            "likeCount": "6327",
            "thumbnailUrl": "https://i.ytimg.com/vi/1rB3hs5INdU/hqdefault.jpg",
            "title": "3 ORANG YANG PERGI KE TEMPAT TERLARANG - Part 3",
            "url": "https://www.youtube.com/watch?v=1rB3hs5INdU",
            "videoId": "1rB3hs5INdU",
            "viewCount": "127557"
        },
        {
            "channelTitle": "Nex Carlos",
            "likeCount": "12432",
            "thumbnailUrl": "https://i.ytimg.com/vi/9yCijDWFIJc/hqdefault.jpg",
            "title": "BARU KALI INI MAKAN SAMPE KE DALEM RUMAH YANG JUAL SAMBIL NONTON TV!!",
            "url": "https://www.youtube.com/watch?v=9yCijDWFIJc",
            "videoId": "9yCijDWFIJc",
            "viewCount": "500247"
        },
        {
            "channelTitle": "Ben Azelart",
            "likeCount": "106353",
            "thumbnailUrl": "https://i.ytimg.com/vi/2lBkf3RupBQ/hqdefault.jpg",
            "title": "I Built a Trampoline Park in My House!",
            "url": "https://www.youtube.com/watch?v=2lBkf3RupBQ",
            "videoId": "2lBkf3RupBQ",
            "viewCount": "10079334"
        },
        {
            "channelTitle": "Dhot Design",
            "likeCount": "160741",
            "thumbnailUrl": "https://i.ytimg.com/vi/UU98RpAfeDo/hqdefault.jpg",
            "title": "LOMBA PART 1 (SPESIAL AGUSTUS) - Animasi Sekolah",
            "url": "https://www.youtube.com/watch?v=UU98RpAfeDo",
            "videoId": "UU98RpAfeDo",
            "viewCount": "3245475"
        },
        {
            "channelTitle": "Solusi BCA",
            "likeCount": "8352",
            "thumbnailUrl": "https://i.ytimg.com/vi/eE9nRV__p-s/hqdefault.jpg",
            "title": "Nurut Apa Kata Mama Season 2 I Episode 4: Barisan Mantan Bu Nyoto",
            "url": "https://www.youtube.com/watch?v=eE9nRV__p-s",
            "videoId": "eE9nRV__p-s",
            "viewCount": "211529"
        },
        {
            "channelTitle": "BIMA Series",
            "likeCount": "12360",
            "thumbnailUrl": "https://i.ytimg.com/vi/2Al4G64hcw0/hqdefault.jpg",
            "title": "BIMA MASUK PENJARA PART 10 (end) - Animasi Drama Series",
            "url": "https://www.youtube.com/watch?v=2Al4G64hcw0",
            "videoId": "2Al4G64hcw0",
            "viewCount": "183285"
        },
        {
            "channelTitle": "SMTOWN",
            "likeCount": "160732",
            "thumbnailUrl": "https://i.ytimg.com/vi/0nPxb9zMBtE/hqdefault.jpg",
            "title": "JAEHYUN \uc7ac\ud604 'Dandelion & Roses' MV",
            "url": "https://www.youtube.com/watch?v=0nPxb9zMBtE",
            "videoId": "0nPxb9zMBtE",
            "viewCount": "962386"
        },
        {
            "channelTitle": "Pebbi Lieyanti",
            "likeCount": "8787",
            "thumbnailUrl": "https://i.ytimg.com/vi/PNe9k4acV94/hqdefault.jpg",
            "title": "BATTLE JAJANAN INDOMARET VS ALFAMART!",
            "url": "https://www.youtube.com/watch?v=PNe9k4acV94",
            "videoId": "PNe9k4acV94",
            "viewCount": "201701"
        },
        {
            "channelTitle": "AHHA RECORDS",
            "likeCount": "24265",
            "thumbnailUrl": "https://i.ytimg.com/vi/CFLFLH7RTbg/hqdefault.jpg",
            "title": "Torang Indonesia - Atta, Aurel, Anang, Ashanty & MALUT Singer (Spesial Kemerdekaan Indonesia)",
            "url": "https://www.youtube.com/watch?v=CFLFLH7RTbg",
            "videoId": "CFLFLH7RTbg",
            "viewCount": "1356522"
        },
        {
            "channelTitle": "Fanny Tjandra",
            "likeCount": "2916",
            "thumbnailUrl": "https://i.ytimg.com/vi/dAnIoRQ9SQc/hqdefault.jpg",
            "title": "Dikejar Kepala yang Suka Marah-Marah!",
            "url": "https://www.youtube.com/watch?v=dAnIoRQ9SQc",
            "videoId": "dAnIoRQ9SQc",
            "viewCount": "181471"
        },
        {
            "channelTitle": "Erick Thohir",
            "likeCount": "4394",
            "thumbnailUrl": "https://i.ytimg.com/vi/2t3EUltby_A/hqdefault.jpg",
            "title": "TC PSSI DI IKN HAMPIR SELESAI!",
            "url": "https://www.youtube.com/watch?v=2t3EUltby_A",
            "videoId": "2t3EUltby_A",
            "viewCount": "193732"
        },
        {
            "channelTitle": "THE FIRST TAKE",
            "likeCount": "206858",
            "thumbnailUrl": "https://i.ytimg.com/vi/EsHQB9gT96k/hqdefault.jpg",
            "title": "aespa - Supernova / THE FIRST TAKE",
            "url": "https://www.youtube.com/watch?v=EsHQB9gT96k",
            "videoId": "EsHQB9gT96k",
            "viewCount": "2288919"
        }
    ],
    "status": 200
}
"""