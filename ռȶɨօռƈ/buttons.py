from .checker import *
from pyrogram.types import (
    InlineKeyboardButton,
    )

def buttonmap(item):
    resolution = item['format']
    if "audio" in resolution:
        return [InlineKeyboardButton(
                f"""
                🎧{resolution}🎧⮞ {vible(item['filesize'])}
                """,
                callback_data=f"""
                ytdata||audio||{item['format_id']}||{item['yturl']}
                """)]
    else:
        return [InlineKeyboardButton(
                f"""
                🎬{resolution}🎬⮞ {vible(item['filesize'])}
                """,
                callback_data=f"""
                ytdata||video||{item['format_id']}||{item['yturl']}
                """)]

def create_buttons(resolutionlist):
    return map(
    buttonmap,
    resolutionlist)