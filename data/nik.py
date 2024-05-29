import random
text = "qwertyuiopasdfghjklzxcvbnm"
emoji = "✌"
fonts = [
         "ⓠⓦⓔⓡⓣⓨⓤⓘⓞⓟⓐⓢⓓⓕⓖⓗⓙⓚⓛⓩⓧⓒⓥⓑⓝⓜ",
         "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶",
         "🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟🅐🅢🅓🅕🅖🅗🅙🅚🅛🅩🅧🅒🅥🅑🅝🅜",
         "𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒",
         "𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕𝚣𝚡𝚌𝚟𝚋𝚗𝚖",
         "ｑｗｅｒｔｙｕｉｏｐａｓｄｆｇｈｊｋｌｚｘｃｖｂｎｍ",
         "⒬⒲⒠⒭⒯⒴⒰⒤⒪⒫⒜⒮⒟⒡⒢⒣⒥⒦⒧⒵⒳⒞⒱⒝⒩⒨",
         "𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞",
         "🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼",
         "𝓆𝓌𝑒𝓇𝓉𝓎𝓊𝒾𝑜𝓅𝒶𝓈𝒹𝒻𝑔𝒽𝒿𝓀𝓁𝓏𝓍𝒸𝓋𝒷𝓃𝓂",
         "𝙦𝙬𝙚𝙧𝙩𝙮𝙪𝙞𝙤𝙥𝙖𝙨𝙙𝙛𝙜𝙝𝙟𝙠𝙡𝙯𝙭𝙘𝙫𝙗𝙣𝙢",
         "𝒒𝒘𝒆𝒓𝒕𝒚𝒖𝒊𝒐𝒑𝒂𝒔𝒅𝒇𝒈𝒉𝒋𝒌𝒍𝒛𝒙𝒄𝒗𝒃𝒏𝒎",
         "qẃéŕtӳúíőṕáśdfǵhjḱĺźxćvbńḿ",
         "QWERTYUIOPASDFGHJKLZXCVBNM"
        ]
def nick_generator(name):
    result = []
    for font in fonts:
        my_name = name
        for i in range (len (text)):
            my_name = my_name.replace(text[i], font[i])
        result.append(my_name)
    return result

# def nick_generator(name):
#     result = []
#     for font in fonts:
#         my_name = name
#         for i in range(len(text)):
#             my_name = my_name.replace(text[i], font[i])
#         e = random.choice(emoji)
#         result.append(e+my_name+e)
#     return result

# "♥q♥w♥e♥r♥t♥y♥u♥i♥o♥p♥a♥s♥d♥f♥g♥h♥j♥k♥l♥z♥x♥c♥v♥b♥n♥m♥"
# "✌𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶✌"
# "█▓▒▒░░░qwertyuiopasdfghjklzxcvbnm░░░▒▒▓█"
# "✩░▒▓▆▅▃▂▁𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥𝐳𝐱𝐜𝐯𝐛𝐧𝐦▁▂▃▅▆▓▒░✩"
# "✴.·´¯`·.·★  🎀𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶🎀  ★·.·`¯´·.✴"
# "¸¸♬·¯·♪·¯·♫¸¸ 𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶¸¸♫·¯·♪¸♩·¯·♬¸¸"