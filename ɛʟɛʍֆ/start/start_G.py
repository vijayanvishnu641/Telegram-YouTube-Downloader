from pyrogram import Client, filters, StopPropagation
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
    )
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_message(filters.group
        &filters.command(
        "ytstart",
        prefixes='/')) 
async def start(
    _,
    ydl: Message
    ):
    usrs = ydl.from_user.first_name
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "🍺 Grðµþ:",
            url="https://t.me/tronxli")],
        [InlineKeyboardButton(
            "📡 ßð†§ Hµß:",
             url="https://t.me/calitrox")],
        [InlineKeyboardButton(
            "🛡 ÇðÐêß¥",
            url="https://t.me/calitronx")],
        [InlineKeyboardButton(
            "🍷 Gï†hµß",
            url="https://github.com/calitronx?tab=repositories")],
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