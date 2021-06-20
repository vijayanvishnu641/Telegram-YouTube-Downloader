from datetime import datetime, timedelta
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
from ʏօʊȶʊɮɛʟɨ import user_time
from ʄɨɢʊʀɛ import youtube_next_fetch
from ռȶɨօռƈ.mpegsdl import extractYt, create_buttons
from աɛɮռʀ import *
import wget
import os
from PIL import Image

@Client.on_message(Filters.regex(ytregex))
async def ytdl(_, message):
    userLastDownloadTime = user_time.get(message.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            wait_time = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
            await message.reply_text(f"`Wait {wait_time} Minutes before next Request`")
            return
    except:
        pass

    url = message.text.strip()
    await message.reply_chat_action("upload_video")
    try:
        title, thumbnail_url, formats = extractYt(url)

        now = datetime.now()
        user_time[message.chat.id] = now + \
                                     timedelta(minutes=youtube_next_fetch)

    except Exception:
        await message.reply_text("Failed To Fetch Youtube Data...😔\n"
                                    "REASON CAN BE:\n"
                                    "-/Due to Copyright"
                                    "./Due to too many requests in server"
                                    "./Due to Link not supported"
                                 )
        return
    buttons = InlineKeyboardMarkup(list(create_buttons(formats)))
    sentm = await message.reply_text("Select Audio or Video👇🏻")
    try:
        img = wget.download(thumbnail_url)
        im = Image.open(img).convert("RGB")
        output_directory = os.path.join(os.getcwd(), "downloads", str(message.chat.id))
        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)
        thumb_image_path = f"{output_directory}.jpg"
        im.save(thumb_image_path,"jpeg")
        await message.reply_photo(thumb_image_path, caption=title, reply_markup=buttons)
        await sentm.delete()
    except Exception as e:
        print(e)
        try:
            thumbnail_url = "https://telegra.ph/file/3f287a7ff7bd6d63fbd60.jpg"
            await message.reply_photo(thumbnail_url, caption=title, reply_markup=buttons)
        except Exception as e:
            await sentm.edit(
            f"<code>{e}</code> #Error")