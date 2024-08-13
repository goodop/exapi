import requests,json

def fancy(text, type=None):
    endpoint = 'https://execross.com/api/v3/fancy'
    headers = {
        'apikey': 'forexecman'
    }
    params = {
        "text" : text,
        "type": type # Optional filter type number: 1 to 35
    }
    responsed = requests.get(endpoint,params=params, headers=headers).json()
    return json.dumps(responsed,ensure_ascii=False,indent=4)

# without type
text = "Ang Ganteng"
data = fancy(text)
print("Response :", data)

# Filter with filter Type
asli = fancy(text,3)
print("Response With Filter type:\n", asli)

'''
Response : {
    "creator": "EXECROSS",
    "ip": "125.164.15.3",
    "result": {
        "text": [
            "Ⓐⓝⓖ Ⓖⓐⓝⓣⓔⓝⓖ",
            "🅐🅝🅖 🅖🅐🅝🅣🅔🅝🅖",
            "Ａｎｇ Ｇａｎｔｅｎｇ",
            "𝐀𝐧𝐠 𝐆𝐚𝐧𝐭𝐞𝐧𝐠",
            "𝕬𝖓𝖌 𝕲𝖆𝖓𝖙𝖊𝖓𝖌",
            "𝑨𝒏𝒈 𝑮𝒂𝒏𝒕𝒆𝒏𝒈",
            "𝓐𝓷𝓰 𝓖𝓪𝓷𝓽𝓮𝓷𝓰",
            "𝔸𝕟𝕘 𝔾𝕒𝕟𝕥𝕖𝕟𝕘",
            "𝙰𝚗𝚐 𝙶𝚊𝚗𝚝𝚎𝚗𝚐",
            "𝖠𝗇𝗀 𝖦𝖺𝗇𝗍𝖾𝗇𝗀",
            "𝗔𝗻𝗴 𝗚𝗮𝗻𝘁𝗲𝗻𝗴",
            "𝘼𝙣𝙜 𝙂𝙖𝙣𝙩𝙚𝙣𝙜",
            "𝘈𝘯𝘨 𝘎𝘢𝘯𝘵𝘦𝘯𝘨",
            "⒜⒩⒢ ⒢⒜⒩⒯⒠⒩⒢",
            "🇦🇳🇬 🇬🇦🇳🇹🇪🇳🇬",
            "🄰🄽🄶 🄶🄰🄽🅃🄴🄽🄶",
            "🅰🅽🅶 🅶🅰🅽🆃🅴🅽🅶",
            "󠁁󠁮󠁧󠀠󠁇󠁡󠁮󠁴󠁥󠁮󠁧",
            "Áńǵ Ǵáńtéńǵ",
            "ﾑ刀g gﾑ刀ｲ乇刀g",
            "คกﻭ ﻭคกՇﻉกﻭ",
            "αηﻭ ﻭαηтєηﻭ",
            "คภﻮ ﻮคภՇєภﻮ",
            "ДиБ БаитэиБ",
            "ልክኗ ኗልክፕቿክኗ",
            "𝔄𝔫𝔤 𝔊𝔞𝔫𝔱𝔢𝔫𝔤",
            "Äṅġ Ġäṅẗëṅġ",
            "ᴀɴɢ ɢᴀɴᴛᴇɴɢ",
            "Ⱥnǥ ǤȺnŧɇnǥ",
            "ₐₙg Gₐₙₜₑₙg",
            "ᴬⁿᵍ ᴳᵃⁿᵗᵉⁿᵍ",
            "ꓯuƃ ⅁ɐuʇǝuƃ",
            "ƃuǝʇuɐ⅁ ƃuꓯ",
            "Aᴎg GAᴎTɘᴎg",
            "gᴎɘTᴎAG gᴎA"
        ]
    },
    "status": 200
}

Response with filter type:
{
    "creator": "EXECROSS",
    "ip": "125.164.15.3",
    "result": {
        "text": "Ａｎｇ Ｇａｎｔｅｎｇ",
        "type": "Fullwidth"
    },
    "status": 200
} 
'''

# Type number:

'''
Fancy Type
1. Circled: ⓔⓧⓐⓜⓟⓛⓔ ⓣⓔⓧⓣ
2. Circled (neg): 🅔🅧🅐🅜🅟🅛🅔 🅣🅔🅧🅣
3. Fullwidth: ｅｘａｍｐｌｅ ｔｅｘｔ
4. Math bold: 𝐞𝐱𝐚𝐦𝐩𝐥𝐞 𝐭𝐞𝐱𝐭
5. Math bold Fraktur: 𝖊𝖝𝖆𝖒𝖕𝖑𝖊 𝖙𝖊𝖝𝖙
6. Math bold italic: 𝒆𝒙𝒂𝒎𝒑𝒍𝒆 𝒕𝒆𝒙𝒕
7. Math bold script: 𝓮𝔁𝓪𝓶𝓹𝓵𝓮 𝓽𝓮𝔁𝓽
8. Math double-struck: 𝕖𝕩𝕒𝕞𝕡𝕝𝕖 𝕥𝕖𝕩𝕥
9. Math monospace: 𝚎𝚡𝚊𝚖𝚙𝚕𝚎 𝚝𝚎𝚡𝚝
10. Math sans: 𝖾𝗑𝖺𝗆𝗉𝗅𝖾 𝗍𝖾𝗑𝗍
11. Math sans bold: 𝗲𝘅𝗮𝗺𝗽𝗹𝗲 𝘁𝗲𝘅𝘁
12. Math sans bold italic: 𝙚𝙭𝙖𝙢𝙥𝙡𝙚 𝙩𝙚𝙭𝙩
13. Math sans italic: 𝘦𝘹𝘢𝘮𝘱𝘭𝘦 𝘵𝘦𝘹𝘵
14. Parenthesized: ⒠⒳⒜⒨⒫⒧⒠ ⒯⒠⒳⒯
15. Regional Indicator: 🇪🇽🇦🇲🇵🇱🇪 🇹🇪🇽🇹
16. Squared: 🄴🅇🄰🄼🄿🄻🄴 🅃🄴🅇🅃
17. Squared (neg): 🅴🆇🅰🅼🅿🅻🅴 🆃🅴🆇🆃
18. Tag: 󠁥󠁸󠁡󠁭󠁰󠁬󠁥󠀠󠁴󠁥󠁸󠁴
19. A-cute: éxáḿṕĺé téxt
20. CJK+Thai: 乇ﾒﾑﾶｱﾚ乇 ｲ乇ﾒｲ
21. Curvy 1: ﻉซค๓ρɭﻉ ՇﻉซՇ
22. Curvy 2: єχαмρℓє тєχт
23. Curvy 3: єאค๓קɭє ՇєאՇ
24. Faux Cyrillic: эхамрlэ тэхт
25. Faux Ethiopic: ቿሸልጠየረቿ ፕቿሸፕ
26. Math Fraktur: 𝔢𝔵𝔞𝔪𝔭𝔩𝔢 𝔱𝔢𝔵𝔱
27. Rock Dots: ëẍäṁṗḷë ẗëẍẗ
28. Small Caps: ᴇxᴀᴍᴩʟᴇ ᴛᴇxᴛ
29. Stroked: ɇxȺmᵽłɇ ŧɇxŧ
30. Subscript: ₑₓₐₘₚₗₑ ₜₑₓₜ
31. Superscript: ᵉˣᵃᵐᵖˡᵉ ᵗᵉˣᵗ
32. Inverted: ǝxɐɯdןǝ ʇǝxʇ
33. Inverted: ʇxǝʇ ǝןdɯɐxǝ
34. Reversed: ɘxAmqlɘ TɘxT
35. Reversed: TxɘT ɘlqmAxɘ
 
'''