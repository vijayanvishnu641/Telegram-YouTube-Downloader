from pyrogram import Client
from Latte import *
from Trial import *
DOWNLOAD_LOCATION = "./Downloads"
TOKEN = Kryogenesis.TOKEN
APP_ID = Kryogenesis.APP_ID
API_HASH = Kryogenesis.API_HASH

Client(
    "ʏօʊȶʊɮɛʟɨ",
    bot_token=TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=20
).run()
