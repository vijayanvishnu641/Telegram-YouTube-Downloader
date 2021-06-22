'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
from IDLER.Trial import *
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
def extractYt(yturl):
    with ydl:
        resolutiontree = []
        r = ydl.extract_info(yturl,
                             download=False)
        for format in r['formats']:
            if not "dash" in str(format['format']).lower():
                resolutiontree.append(
                {
                    "format": format['format'],
                    "filesize": format['filesize'],
                    "format_id": format['format_id'],
                    "yturl": yturl
                    }
                )
        return r['title'], r['thumbnail'], resolutiontree
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'