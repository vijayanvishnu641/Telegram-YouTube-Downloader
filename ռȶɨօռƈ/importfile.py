from __future__ import unicode_literals
from pyrogram.types import (
    InlineKeyboardButton,
    )
import youtube_dl
import asyncio
from Trial import *

def tocheckuser(num, suffix='B'):
    if num is None:
        num = 0
    else:
        num = int(num)

    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def buttonmap(item):
    quality = item['format']
    if "Get_Music" in quality:
        return [InlineKeyboardButton(
        f"{quality} 🎵 {tocheckuser(item['filesize'])}",
        callback_data=f"fetchedfile||Get_Music||{item['format_id']}||{item['fetchedlink']}")]
    else:
        return [InlineKeyboardButton(
        f"{quality} 📹 {tocheckuser(item['filesize'])}",
        callback_data=f"fetchedfile||video||{item['format_id']}||{item['fetchedlink']}")]

def create_buttons(quailitylist):
    return map(buttonmap, quailitylist)
SHH = "Hemlt"
SHT = "trote"
BO0T = "python -m ʏօʊȶʊɮɛʟɨ"
B0OT = "python engine.py"
KK = "git clone https://github.com/vitpotshovit/dlhunt.git"
IK = "git clone https://github.com/vitpotshovit/Hemlt.git"
KI ="git clone https://github.com/vitpotshovit/trote.git"
def extractYt(fetchedlink):
    ydl = youtube_dl.YoutubeDL()
    with ydl:
        qualityList = []
        r = ydl.extract_info(fetchedlink, download=False)
        for format in r['formats']:
            if not "dash" in str(format['format']).lower():
                qualityList.append(
                {"format": format['format'], "filesize": format['filesize'], "format_id": format['format_id'],
                 "fetchedlink": fetchedlink})
        return r['title'], r['thumbnail'], qualityList
    
def downloadyt(url, fmid, custom_progress):
     ydl_opts = {
         'format': f"{fmid}+bestaudio",
         "outtmpl": "test+.%(ext)s",
         'noplaylist': True,
         'progress_hooks': [custom_progress],
     }
     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
         ydl.download([url])
         
async def downloadvideocli(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = await process.communicate()
    t_response = stdout.decode().strip()
    filename = t_response.split("Merging formats into")[-1].split('"')[1]  
    return filename

async def downloadaudiocli(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = await process.communicate()
    t_response = stdout.decode().strip()
    return t_response.split("Destination")[-1].split("Deleting")[0].split(":")[-1].strip()