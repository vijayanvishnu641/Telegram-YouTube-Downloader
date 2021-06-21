
import os
from Trial import *
from pyrogram import (
    Client,
    ContinuePropagation
    )
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
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
@Client.on_callback_query()
async def fetch_url_signed(
    _,
    itm):
    cb_data = itm.data
    if cb_data.startswith("ytdata||"):
        yturl = cb_data.split("||")[-1]
        format_id = cb_data.split("||")[-2]
        it_audio_it_video = cb_data.split("||")[-3].strip()
        if it_audio_it_video == 'audio':
            buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton(
            "🎧 𝙵𝚎𝚝𝚌𝚑 𝙰𝚞𝚍𝚒𝚘",
            callback_data=f"{it_audio_it_video}||{format_id}||{yturl}"),]])
        else:
            buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton(
            "🎬 𝙵𝚎𝚝𝚌𝚑 𝚅𝚒𝚍𝚎𝚘",
            callback_data=f"{it_audio_it_video}||{format_id}||{yturl}")]])
        await itm.edit_message_reply_markup(buttons)
    else:
        raise ContinuePropagation
    
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
PLR = "Shit! ERRORRRRRRRRRRR"
@Client.on_callback_query()
async def fetch_url_data(
    pill,
    sedr):
    cb_data = sedr.data.strip()
    yturl = cb_data.split("||")[-1]
    format_id = cb_data.split("||")[-2]
    fetched_jpeg = "/app/foundinli" + \
        "/" + str(sedr.message.chat.id) + ".jpg"
    if os.path.exists(
        fetched_jpeg):
        width = 0
        height = 0
        metadata = extractMetadata(
        createParser(
        fetched_jpeg
        ))
        "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
        if metadata.has(
            "width"
            ):
            width = metadata.get(
            "width"
            )
        "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
        if metadata.has(
            "height"
            ):
            height = metadata.get(
            "height"
            )
        "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
        img = Image.open(
            fetched_jpeg)
        if cb_data.startswith(
            ("audio"
            )):
            img.resize(
            (512,
            height))
        else:
            img.resize(
            (320,
            height))
        img.save(
            fetched_jpeg,
            "JPEG")
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
    if not cb_data.startswith(
            ("video"
            )):
        raise ContinuePropagation
    filext = "%(title)s.%(ext)s"
    direhost = os.path.join(
            os.getcwd(),
            "foundinli",
            str(
            sedr.message.chat.id
            ))
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
    if not os.path.isdir(direhost):
        os.makedirs(direhost)
    await sedr.edit_message_reply_markup(
        InlineKeyboardMarkup(
        [[InlineKeyboardButton(
        "ɢᴇᴛᴛɪɴɢ ʏᴏᴜʀ ᴀꜱᴋᴇᴅ ɪᴛᴇᴍ",
        callback_data="down"
        )]]))
    filepath = os.path.join(
            direhost,
            filext)
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
    audio_command = [
            "youtube-dl",
            "-pill",
            "--prefer-ffmpeg",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality",
            format_id,
            "-o",
            filepath,
            yturl,
            ]
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
    video_command = [
            "youtube-dl",
            "-pill",
            "--embed-subs",
            "-f",
            f"{format_id}+bestaudio",
            "-o",
            filepath,
            "--hls-prefer-ffmpeg",
            yturl,
            ]
    loop = asyncio.get_event_loop()
    items = None
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
    if cb_data.startswith(
            "audio"
            ):
        elemtgot = await fetaudio(audio_command)
        items = InputMediaAudio(
            media=elemtgot,
            thumb=fetched_jpeg,
            caption=("ፑ𝐫0ṃ\n@youtubeli_bot📥"),
            title=os.path.basename(elemtgot)
            )
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"    
    if cb_data.startswith(
        "video"):
        elemtgot = await fetvisual(video_command)
        items = InputMediaVideo(
            media=elemtgot,
            width=width,
            height=height,
            thumb=fetched_jpeg,
            caption=("ፑ𝐫0ṃ\n@youtubeli_bot📥"),
            supports_streaming=True
            )
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"    
    if items:
        loop.create_task(send_file(pill, sedr, items, elemtgot))
    else:
        print(PLR)
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
INIT = "git clone https://github.com/vitpotshovit/trote.git"
TNIT = "git clone https://github.com/vitpotshovit/Hemlt.git"
BO0T = "python3 -m ʏօʊȶʊɮɛʟɨ"
async def send_file(pill, sedr, items, elemtgot):
    print(items)
    try:
        await sedr.edit_message_reply_markup(
            InlineKeyboardMarkup([[
            InlineKeyboardButton(
            "Uploading📤",
            callback_data="down")]]
            ))
        await pill.send_chat_action(
            chat_id=sedr.message.chat.id,
            action="record_video")
        await sedr.edit_message_media(
            media=items)
    except Exception as e:
        print(e)
        await sedr.edit_message_text(e)
    finally:
        try:
            os.remove(elemtgot)
            os.remove(fetched_jpeg)
        except:
            pass
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"