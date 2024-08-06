import telebot
import requests
import os
import webbrowser

webbrowser.open('https://t.me/kwulu')

try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')

d = "Frost"

sif = render(f'{d}', colors=['red', 'yellow'], align='center')
print(sif)

bot_token = "688803725806:AAHFKJ_ejEovfmSUIflqwkO5QOl"  # قم بوضع توكن البوت الخاص بك هنا

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "أهلاً بك! قم بإرسال اسم المستخدم الخاص بالضحية على إنستغرام! 🥷⚡",
                     parse_mode='Markdown',
                     reply_markup=telebot.types.InlineKeyboardMarkup().add(
                         telebot.types.InlineKeyboardButton(text="قناة البوت 🔰", url="https://t.me/kwulu")
                     ))


@bot.message_handler(func=lambda message: True)
def get_user_info(message):
    user = message.text.strip()
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar',
        'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
    }
    urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
    re = requests.get(urlg, headers=headers).json()
    bio = re["data"]["user"]["biography"]
    followers = re["data"]["user"]["edge_followed_by"]["count"]
    following = re["data"]["user"]["edge_follow"]["count"]
    name = re["data"]["user"]["full_name"]
    user_id = re["data"]["user"]["id"]
    posts = re["data"]["user"]["edge_owner_to_timeline_media"]["count"]
    date = requests.get(f"https://o7aa.pythonanywhere.com/?id={user_id}").json()["date"]
    profile_pic = re["data"]["user"]["profile_pic_url_hd"]
    tlg = f"""
⌯ تم سحب معلومات الضحية بنجاح ✅ ⌯ 
. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .
[💙] الإسم ➥ {name}
[👻] اسم المستخدم ➥ {user}
[👥] المتابعون ➥ {followers}
[🗣] المتابعين ➥ {following}
[🆔] المعرف ➥ {user_id}
[👻] البايو ➥ {bio}
[💞] المنشورات ➥ {posts}
[⏱] التاريخ ➥ {date}
. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .
⚖️ Telegram: @[Frost_0001]\n⚖️ CH: @kwulu
"""
    bot.send_photo(message.chat.id, profile_pic, caption=tlg, parse_mode='Markdown')


bot.polling()