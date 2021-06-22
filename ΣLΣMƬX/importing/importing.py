'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
import os
from IDLER.Trial import *
from pyrogram import Client, ContinuePropagation
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaVideo,
    InputMediaAudio,
    )
from ПKΛ匚 import *
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from ʏօʊȶʊɮɛʟɨ import *
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_callback_query()
async def catch_youtube_fmtid(
    _,
    m):
    feeder_infos = m.data
    if feeder_infos.startswith("ytdata||"):
        yturl = feeder_infos.split("||")[-1]
        format_id = feeder_infos.split("||")[-2]
        media_type = feeder_infos.split("||")[-3].strip()
        if media_type == 'audio':
            buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton("📥    ÐðwñlðåÐ ÄµÐïð  🎤",
                                 callback_data=f"{media_type}||{format_id}||{yturl}"),]])
        else:
            buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton("📥    ÐðwñlðåÐ VïÐêð  🎨",
                                 callback_data=f"{media_type}||{format_id}||{yturl}")]])
        await m.edit_message_reply_markup(buttons)
    else:
        raise ContinuePropagation
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_callback_query()
async def catch_youtube_dldata(
    c,
    q):
    feeder_infos = q.data.strip()
    yturl = feeder_infos.split("||")[-1]
    format_id = feeder_infos.split("||")[-2]
    jpeg_fetched = DLDR + \
        "/" + str(q.message.chat.id) + ".jpg"
    if os.path.exists(jpeg_fetched):
        width = 0
        height = 0
        metadata = extractMetadata(createParser(jpeg_fetched))
        if metadata.has(
            "width"):
            width = metadata.get(
            "width")
        if metadata.has(
            "height"):
            height = metadata.get(
            "height")
        img = Image.open(
            jpeg_fetched)
        if feeder_infos.startswith((
            "audio",)):
            img.resize((
            512,
            height))
        else:
            img.resize((
            512,
            height))
        img.save(jpeg_fetched, "JPEG")
    if not feeder_infos.startswith((
            "video",
            "audio",)):
        raise ContinuePropagation
    filext = "%(title)s.%(ext)s"
    userdir = os.path.join(os.getcwd(), DLD, str(q.message.chat.id))
    if not os.path.isdir(userdir):
        os.makedirs(userdir)
    await q.edit_message_reply_markup(
        InlineKeyboardMarkup([[
            InlineKeyboardButton(
            "🏷ᴡᴀɪᴛ ᴛɪᴍᴇ ᴅᴇᴘᴇɴᴅꜱ ᴏɴ ꜱɪᴢᴇ ᴏꜰ ᴍᴇᴅɪᴀ",
        callback_data="down")]]))
    filepath = os.path.join(
        userdir,
        filext)
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    audioseeder_type = [
        "youtube-dl",
        "-c",
        "--prefer-ffmpeg",
        "--extract-audio",
        "--audio-format",
        "mp3",
        "--audio-quality",
        format_id,
        "-o",
        filepath,
        yturl,
        ]
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    videoseeder_type = [
        "youtube-dl",
        "-c",
        "--embed-subs",
        "-f",
        f"{format_id}+bestaudio",
        "-o",
        filepath,
        "--hls-prefer-ffmpeg",
        yturl,
        ]
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    if feeder_infos.startswith(
        "audio"):
        item_id = await audioseeder(
            audioseeder_type)
        med = InputMediaAudio(
            media=item_id,
            thumb=jpeg_fetched,
            caption=(POWEREDA),
            title=os.path.basename(item_id)
        )
    if feeder_infos.startswith(
        "video"):
        item_id = await videoseeder(
            videoseeder_type)
        med = InputMediaVideo(
            media=item_id,
            width=width,
            height=height,
            thumb=jpeg_fetched,
            caption=(POWEREDV),
            supports_streaming=True
        )
    if med:
        loop.create_task(
            send_file(
                c,
                q,
                med,
                item_id))
    else:
        print("media not found")
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
async def send_file(c, q, med, item_id):
    print(med)
    try:
        await q.edit_message_reply_markup(
                 InlineKeyboardMarkup([[
                InlineKeyboardButton(
                "Uploading📤",
                callback_data="down")
                ]]))
        await c.send_chat_action(chat_id=q.message.chat.id, action="record_video")
        await q.edit_message_media(media=med)
    except Exception as e:
        print(e)
        await q.edit_message_text(e)
    finally:
        try:
            os.remove(item_id)
            os.remove(jpeg_fetched)
        except:
            print(CALIBR)
            pass
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'