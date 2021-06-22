
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

@Client.on_callback_query()
async def catch_youtube_fmtid(_, m):
    cb_data = m.data
    if cb_data.startswith("ytdata||"):
        yturl = cb_data.split("||")[-1]
        format_id = cb_data.split("||")[-2]
        media_type = cb_data.split("||")[-3].strip()
        print(media_type)
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

@Client.on_callback_query()
async def catch_youtube_dldata(c, q):
    cb_data = q.data.strip()
    yturl = cb_data.split("||")[-1]
    format_id = cb_data.split("||")[-2]
    thumb_image_path = "/app/downloads/" + \
        "/" + str(q.message.chat.id) + ".jpg"
    if os.path.exists(thumb_image_path):
        width = 0
        height = 0
        metadata = extractMetadata(createParser(thumb_image_path))
        if metadata.has(
            "width"):
            width = metadata.get(
            "width")
        if metadata.has(
            "height"):
            height = metadata.get(
            "height")
        img = Image.open(
            thumb_image_path)
        if cb_data.startswith((
            "audio",)):
            img.resize((
            90,
            height))
        else:
            img.resize((
            512,
            height))
        img.save(thumb_image_path, "JPEG")
    if not cb_data.startswith((
            "video",
            "audio",)):
        print("no data found")
        raise ContinuePropagation
    filext = "%(title)s.%(ext)s"
    userdir = os.path.join(os.getcwd(), "downloads", str(q.message.chat.id))
    if not os.path.isdir(userdir):
        os.makedirs(userdir)
    await q.edit_message_reply_markup(
        InlineKeyboardMarkup([[
            InlineKeyboardButton(
            "🏷ᴡᴀɪᴛ ᴛɪᴍᴇ ᴅᴇᴘᴇɴᴅꜱ ᴏɴ ꜱɪᴢᴇ ᴏꜰ ᴍᴇᴅɪᴀ",
        callback_data="down")]]))
    filepath = os.path.join(userdir, filext)
    audio_command = [
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

    video_command = [
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
    loop = asyncio.get_event_loop()
    med = None
    if cb_data.startswith("audio"):
        filename = await downloadaudiocli(
            audio_command)
        med = InputMediaAudio(
            media=filename,
            thumb=thumb_image_path,
            caption=(POWEREDA),
            supports_streaming=True,
            title=os.path.basename(filename)
        )

    if cb_data.startswith("video"):
        filename = await downloadvideocli(
            video_command)
        med = InputMediaVideo(
            media=filename,
            width=width,
            height=height,
            thumb=thumb_image_path,
            caption=(POWEREDV),
            supports_streaming=True
        )
    if med:
        loop.create_task(send_file(c, q, med, filename))
    else:
        print("media not found")

async def send_file(c, q, med, filename):
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
            os.remove(filename)
            os.remove(thumb_image_path)
        except:
            pass