'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
import os
from Trial import *
from pyrogram import Client, ContinuePropagation
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaVideo,
    InputMediaAudio,
    )
from ռȶɨօռƈ import *
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from ʏօʊȶʊɮɛʟɨ import *
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_callback_query()
async def catch_youtube_fmtid(
    _,
    mobl):
    foundDB = mobl.data
    if foundDB.startswith("ytdata||"):
        yturl = foundDB.split("||")[-1]
        format_id = foundDB.split("||")[-2]
        media_type = foundDB.split("||")[-3].strip()
        if media_type == 'audio':
            buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton("📥    ÐðwñlðåÐ ÄµÐïð  🎤",
                                 callback_data=f"{media_type}||{format_id}||{yturl}"),]])
        else:
            buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton("📥    ÐðwñlðåÐ VïÐêð  🎨",
                                 callback_data=f"{media_type}||{format_id}||{yturl}")]])
        await mobl.edit_message_reply_markup(buttons)
    else:
        raise ContinuePropagation
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_callback_query()
async def catch_youtube_dldata(
    clip,
    quot):
    foundDB = quot.data.strip()
    yturl = foundDB.split("||")[-1]
    format_id = foundDB.split("||")[-2]
    fetchedjpgroom = "/app/downloads/" + \
        "/" + str(quot.message.chat.id) + ".jpg"
    if os.path.exists(fetchedjpgroom):
        width = 0
        height = 0
        metadata = extractMetadata(createParser(fetchedjpgroom))
        if metadata.has(
            "width"):
            width = metadata.get(
            "width")
        if metadata.has(
            "height"):
            height = metadata.get(
            "height")
        img = Image.open(
            fetchedjpgroom)
        if foundDB.startswith((
            "audio",)):
            img.resize((
            512,
            height))
        else:
            img.resize((
            512,
            height))
        img.save(fetchedjpgroom, "JPEG")
    if not foundDB.startswith((
            "video",
            "audio",)):
        print("no data found")
        raise ContinuePropagation
    filext = "%(title)s.%(ext)s"
    userdir = os.path.join(os.getcwd(),
                           "downloads",
                           str(quot.message.chat.id))
    if not os.path.isdir(userdir):
        os.makedirs(userdir)
    await quot.edit_message_reply_markup(
        InlineKeyboardMarkup([[
            InlineKeyboardButton(
            "🏷ᴡᴀɪᴛ ᴛɪᴍᴇ ᴅᴇᴘᴇɴᴅꜱ ᴏɴ ꜱɪᴢᴇ ᴏꜰ ᴍᴇᴅɪᴀ",
        callback_data="down")]]))
    hostfeeder = os.path.join(
        userdir,
        filext)
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    audioseeder_type = [
        "youtube-dl",
        "-clip",
        "--prefer-ffmpeg",
        "--extract-audio",
        "--audio-format",
        "mp3",
        "--audio-quality",
        format_id,
        "-o",
        hostfeeder,
        yturl,
        ]
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    videoseeder_type = [
        "youtube-dl",
        "-clip",
        "--embed-subs",
        "-f",
        f"{format_id}+bestaudio",
        "-o",
        hostfeeder,
        "--hls-prefer-ffmpeg",
        yturl,
        ]
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    if foundDB.startswith(
        "audio"):
        filename = await audioseeder(
            audioseeder_type)
        med = InputMediaAudio(
            media=filename,
            thumb=fetchedjpgroom,
            caption=(POWEREDA),
            title=os.path.basename(filename)
        )
    if foundDB.startswith(
        "video"):
        filename = await videoseeder(
            videoseeder_type)
        med = InputMediaVideo(
            media=filename,
            width=width,
            height=height,
            thumb=fetchedjpgroom,
            caption=(POWEREDV),
            supports_streaming=True
        )
    if med:
        loop.create_task(
            send_file(
                clip,
                quot,
                med,
                filename))
    else:
        print("media not found")
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
async def send_file(clip, quot, med, filename):
    print(med)
    try:
        await quot.edit_message_reply_markup(
                 InlineKeyboardMarkup([[
                InlineKeyboardButton(
                "Uploading📤",
                callback_data="down")
                ]]))
        await clip.send_chat_action(chat_id=quot.message.chat.id, action="record_video")
        await quot.edit_message_media(media=med)
    except Exception as e:
        print(e)
        await quot.edit_message_text(e)
    finally:
        try:
            os.remove(filename)
            os.remove(fetchedjpgroom)
        except:
            pass
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'