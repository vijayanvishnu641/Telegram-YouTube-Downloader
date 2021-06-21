from datetime import datetime, timedelta
from pyrogram import Client, filters
from ռȶɨօռƈ import *
from pyrogram.types import Message
import wget
import os
from PIL import Image
from Trial import *
from pyrogram.types import (
    InlineKeyboardMarkup,
    )

@Client.on_message(filters.regex(ytregex))
async def ytdl(_, ydl: Message):
    userLastDownloadTime = user_time.get(ydl.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            wait_time = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
            await ydl.reply_text(f"`Wait {wait_time} Minutes before next Request`")
            return
    except:
        pass

    url = ydl.text.strip()
    await ydl.reply_chat_action("upload_video")
    try:
        title, thumbnail_url, formats = extractYt(url)

        now = datetime.now()
        user_time[ydl.chat.id] = now + \
                                     timedelta(minutes=wait_son)

    except Exception:
        await ydl.reply_text("`Failed To Fetch Youtube Data...😔\nWait for {wait_time} or try other link")
        return
    buttons = InlineKeyboardMarkup(list(create_buttons(formats)))
    sentm = await ydl.reply_text("Select Audio or Video👇🏻")
    try:
        img = wget.download(thumbnail_url)
        im = Image.open(img).convert("RGB")
        output_directory = os.path.join(os.getcwd(), "downloads", str(ydl.chat.id))
        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)
        thumb_image_path = f"{output_directory}.jpg"
        im.save(thumb_image_path,"jpeg")
        await ydl.reply_photo(thumb_image_path, caption=title, reply_markup=buttons)
        await sentm.delete()
    except Exception as e:
        print(e)
        try:
            thumbnail_url = "https://telegra.ph/file/ed28706fff93c4a2956e5.jpg"
            await ydl.reply_photo(thumbnail_url, caption=title, reply_markup=buttons)
        except Exception as e:
            await sentm.edit(
            f"<code>{e}</code> #Error")
