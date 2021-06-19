from pyrogram import *
from աɛɮռʀ import *
from ʄɨɢʊʀɛ.config import *

TOKEN = Kati.TOKEN
APP_ID = Kati.APP_ID
API_HASH = Kati.API_HASH

plugins = dict(
    root="ɛʟɛʍֆ",
)

Client(
    "YouTubeDlBot",
    bot_token=TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=100
).run()
