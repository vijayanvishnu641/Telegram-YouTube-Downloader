from pyrogram import Client
import config

DOWNLOAD_LOCATION = "./Downloads"

TOKEN = config.TOKEN
APP_ID = config.APP_ID
API_HASH = config.API_HASH

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
