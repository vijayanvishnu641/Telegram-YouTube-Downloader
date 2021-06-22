from __future__ import unicode_literals
import asyncio
from Trial import *
from pyrogram.types import (
    InlineKeyboardButton,
    )
import youtube_dl

def vible(num, suffix='B'):
    if num is None:
        num = 0
    else:
        num = int(num)

    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def buttonmap(fetchedfiles):
    resolution = fetchedfiles['format']
    if "audio" in resolution:
        return [InlineKeyboardButton(f"🎧{resolution}🎧⮞ {vible(fetchedfiles['filesize'])}",
                                     callback_data=f"ytdata||audio||{fetchedfiles['format_id']}||{fetchedfiles['yturl']}")]
    else:
        return [InlineKeyboardButton(f"🎬{resolution}🎬⮞ {vible(fetchedfiles['filesize'])}",
                                     callback_data=f"ytdata||video||{fetchedfiles['format_id']}||{fetchedfiles['yturl']}")]

def create_buttons(resolutiontree):
    return map(buttonmap, resolutiontree)

def downloadyt(url, fmid, custom_progress):
     ydl_opts = {
         'format': f"{fmid}+bestaudio",
         "outtmpl": "test+.%(ext)s",
         'noplaylist': True,
         'progress_hooks': [custom_progress],
     }
     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
         ydl.download([url])
         
def extractYt(yturl):
    ydl = youtube_dl.YoutubeDL()
    with ydl:
        resolutiontree = []
        r = ydl.extract_info(yturl, download=False)
        for format in r['formats']:
            if not "dash" in str(format['format']).lower():
                resolutiontree.append(
                {"format": format['format'], "filesize": format['filesize'], "format_id": format['format_id'],
                 "yturl": yturl})

        return r['title'], r['thumbnail'], resolutiontree

async def downloadvideocli(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    print(e_response)
    filename = t_response.split("Merging formats into")[-1].split('"')[1]
    
    return filename


async def downloadaudiocli(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    print("Download error:", e_response)

    return t_response.split("Destination")[-1].split("Deleting")[0].split(":")[-1].strip()
