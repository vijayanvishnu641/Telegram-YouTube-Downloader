
import os
from Trial import *
from pyrogram import Client, ContinuePropagation
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaVideo,
    InputMediaAudio
    )
from ռȶɨօռƈ import *
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser


@Client.on_callback_query()
async def catch_youtube_fmtid(
    _,
    buta):
    fetch_elems = buta.data
    if fetch_elems.startswith("fetchedfile||"):
        fetchedlink = fetch_elems.split("||")[-1]
        gotfilekey = fetch_elems.split("||")[-2]
        media_type = fetch_elems.split("||")[-3].strip()
        print(media_type)
        if media_type == 'Get_Music':
            pod = InlineKeyboardMarkup(
                [[InlineKeyboardButton(
                "Best-Mp3",
                callback_data=f"{media_type}||{gotfilekey}||{fetchedlink}")]])
        else:
            pod = InlineKeyboardMarkup(
                [[InlineKeyboardButton(
                "Best-Mp4",
                callback_data=f"{media_type}||{gotfilekey}||{fetchedlink}")]])
        await buta.edit_message_reply_markup(pod)
    else:
        raise ContinuePropagation

@Client.on_callback_query()
async def catch_youtube_dldata(
    fetch,
    data_pod):
    fetch_elems = data_pod.data.strip()
    fetchedlink = fetch_elems.split("||")[-1]
    gotfilekey = fetch_elems.split("||")[-2]
    urljpegclone = "/ytliBot/fetcheditem" + \
        "/" + str(data_pod.message.chat.id) + ".jpeg"
    print(urljpegclone)
    if os.path.exists(urljpegclone):
        width = 0
        height = 0
        metadata = extractMetadata(createParser(urljpegclone))
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        img = Image.open(urljpegclone)
        if fetch_elems.startswith((
            "Get_Music",
            )):
            img.resize((320, height))
        else:
            img.resize((90, height))
        img.save(urljpegclone, "JPEG")
    if not fetch_elems.startswith((
        "video",
        "Get_Music",
        )):
        print("no data found")
        raise ContinuePropagation

    filext = "%(title)s.%(ext)s"
    imported_host = os.path.join(os.getcwd(), "fetcheditem", str(data_pod.message.chat.id))

    if not os.path.isdir(imported_host):
        os.makedirs(imported_host)
    await data_pod.edit_message_reply_markup(
        InlineKeyboardMarkup(
        [[InlineKeyboardButton(
        "Getting BEST_QUALITY💋",
        callback_data="down")
        ]]))
    filepath = os.path.join(imported_host, filext)
    await data_pod.edit_message_reply_markup([[InlineKeyboardButton("Processing..")]])

    audio_command = [
        "youtube-dl",
        "-fetch",
        "--prefer-ffmpeg",
        "--extract-Get_Music",
        "--Get_Music-format", "mp3",
        "--Get_Music-quality", gotfilekey,
        "-o", filepath,
        fetchedlink,
    ]
    video_command = [
        "youtube-dl",
        "-fetch",
        "--embed-subs",
        "-f", f"{gotfilekey}+bestaudio",
        "-o", filepath,
        "--hls-prefer-ffmpeg", fetchedlink]
    item_spawned = None
    
    if fetch_elems.startswith("Get_Music"):
        filename = await downloadaudiocli(audio_command)
        item_spawned = InputMediaAudio(
            media=filename,
            thumb=urljpegclone,
            caption=(
            "ፑ𝐫0ṃ\n@YoutubeDownloadVrtx_Bot📥"
            ),
            title=os.path.basename(filename)
            )

    if fetch_elems.startswith("video"):
        filename = await downloadvideocli(video_command)
        dur = round(duration(filename))
        item_spawned = InputMediaVideo(
            media=filename,
            duration=dur,
            width=width,
            height=height,
            thumb=urljpegclone,
            caption=(
            "ፑ𝐫0ṃ\n@YoutubeDownloadVrtx_Bot📥"
            ),
            supports_streaming=True
        )

    if item_spawned:
        loop.create_task(fetchedfile_throw(
        fetch,
        data_pod,
        item_spawned,
        filename))
    else:
        print(
        "media not found"
        )

async def fetchedfile_throw(
    fetch,
    data_pod,
    item_spawned,
    filename):
    print(item_spawned)
    try:
        await data_pod.edit_message_reply_markup(
                 InlineKeyboardMarkup([[InlineKeyboardButton("Uploading📤", callback_data="down")]])          
            )
        await fetch.send_chat_action(chat_id=data_pod.message.chat.id, action="record_video")
        await data_pod.edit_message_media(media=item_spawned)
    except Exception as e:
        print(e)
        await data_pod.edit_message_text(e)
    finally:
        try:
            os.remove(filename)
            os.remove(urljpegclone)
        except:
            pass
