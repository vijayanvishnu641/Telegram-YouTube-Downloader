'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import Message
from Trial import *
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_message(
    filters.command(
        "link",
        prefixes='/')) 
async def link(
    _,
    ydl: Message
    ):
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("", url="https://t.me/")],
        [InlineKeyboardButton(":", url="https://t.me/")],
        [InlineKeyboardButton(":", url="https://t.me/")],
        [InlineKeyboardButton(":", url="https://t.me/")],
        [InlineKeyboardButton(":", url="https://t.me/")]
    ])
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
    await ydl.reply_photo(
        youliurl,
        reply_markup=joinButton,
        caption=youtube_ex
        )
    raise StopPropagation
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'