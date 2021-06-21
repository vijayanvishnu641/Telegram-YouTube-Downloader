from pyrogram import Client
import os

# class Kati:
#     TOKEN = "1869507072:AAFzDcb5uwVwO7a59vlrf0H9e5crSh_lZM4"
#     APP_ID = 6372795
#     API_HASH = "4b7731b0a6d8e15bef82863887feb293"
#     CHECK = "YES"
class Kati:
    TOKEN = os.environ.get("TOKEN")
    APP_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")

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
