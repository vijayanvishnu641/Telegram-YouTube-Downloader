from . import *
import youtube_dl

def extractYt(yturl):
    ydl = youtube_dl.YoutubeDL()
    with ydl:
        qualityList = []
        r = ydl.extract_info(yturl, download=False)
        for format in r['formats']:
            if not "dash" in str(format['format']).lower():
                qualityList.append(
                {"format": format['format'], "filesize": format['filesize'], "format_id": format['format_id'],
                 "yturl": yturl})

        return r['title'], r['thumbnail'], qualityList