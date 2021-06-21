from datetime import datetime, timedelta
from pyrogram import Client, filters
from ռȶɨօռƈ import *
from pyrogram.types import Message
import wget
import os
from ʏօʊȶʊɮɛʟɨ import *
from PIL import Image
from Trial import *
from pyrogram.types import (
    InlineKeyboardMarkup,
    )
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
@Client.on_message(
    filters.regex(ytregex)
    )
async def ytdl(
    _,
    ydl: Message
    ):
    userLastDownloadTime = user_time.get(
    ydl.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            await ydl.reply_text(f"`Wait a few seconds before next Request`")
            return
    except:
        pass
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
    url = ydl.text.strip()
    await ydl.reply_chat_action("recording_video")
    try:
        title, thumbnail_url, formats = extractYt(url)
        now = datetime.now()
        user_time[ydl.chat.id] = now + \
        timedelta(seconds=wait_son)
    except Exception:
        await ydl.reply_text(f"`Wait for few seconds or try other link`")
        return
    pod = InlineKeyboardMarkup(list(inlinefeeder(formats)))
    sentm = await ydl.reply_text("Select Best-Mp3 or Best-Mp4👇🏻")
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
    try:
        img = wget.download(thumbnail_url)
        im = Image.open(img).convert("RGB")
        output_directory = os.path.join(
            os.getcwd(),
            "foundinli",
            str(ydl.chat.id))
        if not os.path.isdir(
            output_directory):
            os.makedirs(
            output_directory)
        urljpegclone = f"{output_directory}.jpg"
        im.save(
            urljpegclone,
            "jpeg")
        await ydl.reply_photo(
            urljpegclone,
            caption=title,
            reply_markup=pod)
        await sentm.delete()
    except Exception as e:
        print(e)
        try:
            thumbnail_url = youliurl
            await ydl.reply_photo(
                thumbnail_url,
                caption=title,
                reply_markup=pod)
        except Exception as e:
            await sentm.edit(
            f"<code>{e}</code> #Error")
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"