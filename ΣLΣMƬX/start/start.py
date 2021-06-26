'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
    )
from IDLER.Trial import *
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
B0Ot = "python engine.py"
@Client.on_message(
    filters.private
    &filters.command(
    "start",
    prefixes='/')) 
async def start(
    _,
    ydl: Message
    ):
    usrs = ydl.from_user.first_name
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "🍺 Grðµþ:",
            url="https://t.me/hypevoids")],
        [InlineKeyboardButton(
            "📡 ßð†§ Hµß:",
             url="https://t.me/hypevoidlab")],
        [InlineKeyboardButton(
            "🛡 ÇðÐêß¥",
            url="https://t.me/HypeVoidSoul")],
        [InlineKeyboardButton(
            "🍷 Gï†hµß",
            url="https://github.com/HypeVoidSoul?tab=repositories")],
            ])
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    welcomed = f"""
🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟

🎈Dear,
Sir,Ma'am  <b>{usrs}</b>

Use the below button or type /help for More info.

🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟
"""
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    await ydl.reply_photo(
        youliurl,
        caption=welcomed,
        reply_markup=joinButton)
    raise StopPropagation
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'