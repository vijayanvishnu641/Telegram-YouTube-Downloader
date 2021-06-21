from pyrogram.types import (
    InlineKeyboardButton,
    )
from .checkuser import *
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
def buttonmap(item):
    quality = item['format']
    if "audio" in quality:
        return [InlineKeyboardButton(f"""
        {quality} 🎵 {tocheckuser(item['filesize'])}""",
        callback_data=f"""
        ytdata||audio||{item['format_id']}||{item['yturl']}
        """)]
    else:
        return [InlineKeyboardButton(f"""
        {quality} 📹 {tocheckuser(item['filesize'])}""",
        callback_data=f"""
        ytdata||video||{item['format_id']}||{item['yturl']}
        """)]

def inlinefeeder(amount):
    return map(
        buttonmap,
        amount)
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"