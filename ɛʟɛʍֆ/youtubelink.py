from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
from աɛɮռʀ import *

@Client.on_message(Filters.command(["youtubelink"]), group=-2)
async def love(_, message):
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍕𝗘𝗗𝗠🍕", url="https://t.me/joinchat/iltGypPXEbNhODY1")],
        [InlineKeyboardButton("🍤𝗟𝗼-𝗙𝗶🍤:", url="https://t.me/joinchat/A59waiPeCeQ5ODJl")],
        [InlineKeyboardButton("🍨𝗧𝗥𝗔𝗣.𝗕𝗘𝗔𝗧🍨:", url="https://t.me/joinchat/1xzYUF0HdFw3N2Fl")],
        [InlineKeyboardButton("🌭𝗡𝗖𝗦🌭:", url="https://t.me/joinchat/aHN50rUyUgphMDll")],
        [InlineKeyboardButton("🍪𝗣𝗢𝗣🍪:", url="https://t.me/joinchat/yVpEI2q4U3NmZDBl")]
    ])
    youtube_ex = f"""
**Some example youtube channels and songs if you don't know what u want**📺
- type /love if i helped u anyway🍗🍔🍟🍕
```ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ``` """
    await message.reply_text(youtube_ex, reply_markup=joinButton)
    raise StopPropagation