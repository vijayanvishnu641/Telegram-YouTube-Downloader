'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
from datetime import datetime, timedelta
from pyrogram import Client, filters
from ПKΛ匚 import *
from pyrogram.types import Message
import wget
import os
from ʏօʊȶʊɮɛʟɨ import *
from PIL import Image
from IDLER.Trial import *
from pyrogram.types import (
    InlineKeyboardMarkup,
    )
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_message(
    filters.regex(
        ytregex))
async def ytdl(
    _,
    ydl: Message
    ):
    userLastDownloadTime = user_time.get(ydl.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            await ydl.reply_text(
                f"`Wait a few min Minutes before next Request`")
            return
    except:
        pass
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    url = ydl.text.strip()
    await ydl.reply_chat_action("record_video")
    try:
        title, fetchedimage, formats = extractYt(url)
        user_time[ydl.chat.id] = now + \
        timedelta(minutes=wait_son)
    except Exception:
        await ydl.reply_text(f"`Wait for a few min or try other link`")
        return
    pod = InlineKeyboardMarkup(list(resmaker(formats)))
    try:
        img = wget.download(fetchedimage)
        im = Image.open(img).convert("RGB")
        hostsend = os.path.join(os.getcwd(), "downloads", str(ydl.chat.id))
        if not os.path.isdir(hostsend):
            os.makedirs(hostsend)
        urljpegclone = f"{hostsend}.jpg"
        im.save(
            urljpegclone,
            "jpeg")
        await ydl.reply_photo(urljpegclone, caption=title, reply_markup=pod)
    except Exception as e:
        print(e)
        try:
            fetchedimage = youliurl
            await ydl.reply_photo(
                fetchedimage,
                caption=title,
                reply_markup=pod)
        except Exception as e:
            await ydl.reply_text(
            f"<code>{e}</code> #Error")
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'