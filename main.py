import requests
from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    22658021,
    6da533e7c45bc668182b5a0f5a4497dd,
    bot_token=7740237222:AAEUJJBK7iLOMYTsox9epp7iG2unPQvYXmY,
    plugins=dict(root="handlers"),
)

print("[INFO]: CYBERMUSIC STARTED!")

bot.start()
run()
