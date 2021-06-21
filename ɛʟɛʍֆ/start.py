from pyrogram import Client, filters, StopPropagation
from pyrogram.types import Message
from Trial import *
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
@Client.on_message(
    filters.command("start", prefixes='/')
                   ) 
async def start(
    _,
    ydl: Message
    ):
    usrs = ydl.from_user.first_name
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Group:", url="https://t.me/tronxli")],
        [InlineKeyboardButton("Bot update:", url="https://t.me/calitrox")],
        [InlineKeyboardButton("Owner", url="https://t.me/calitronx")],
    ])
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
    welcomed = f"""
🎈Dear,
Sir,Ma'am  <b>{usrs}</b>

Use the below button or type /help for More info.
"""
    "|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
    await ydl.reply_photo(
        youliurl,
        caption=welcomed,
        reply_markup=joinButton)
    raise StopPropagation
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"