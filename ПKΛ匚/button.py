'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
from pyrogram.types import (
    InlineKeyboardButton,
    )
from .vible import *
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
def resshaper(fetchedfiles):
    resolution = fetchedfiles['format']
    if "audio" in resolution:

        return [InlineKeyboardButton(f"🎧{resolution}🍩{vible(fetchedfiles['filesize'])}🍩",
                                     callback_data=f"ytdata||audio||{fetchedfiles['format_id']}||{fetchedfiles['yturl']}")]
    else:
        return [InlineKeyboardButton(f"🎬{resolution}🍿{vible(fetchedfiles['filesize'])}🍿",
                                     callback_data=f"ytdata||video||{fetchedfiles['format_id']}||{fetchedfiles['yturl']}")]

def resmaker(resolutiontree):
    return map(resshaper, resolutiontree)
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'