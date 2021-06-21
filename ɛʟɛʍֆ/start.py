from pyrogram import Client, filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
from Trial import *
@Client.on_message(filters.command(["start"]), group=-2)
async def start(_, message):
    usrs = message.from_user.first_name
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⛓**𝔾𝕣𝕠𝕦𝕡**⛓:", url="https://t.me/tronxli")],
        [InlineKeyboardButton("⚙️**⚙𝕌𝕡𝕕𝕒𝕥𝕖_ℂ𝕙𝕒𝕟𝕟𝕖𝕝**⚙️:", url="https://t.me/calitrox")],
        [InlineKeyboardButton("📨**𝔾𝕚𝕥ℍ𝕦𝕓**📨", url="https://t.me/calitrox")],
        [InlineKeyboardButton("🧬**𝕆𝕨𝕟𝕖𝕣**🧬", url="https://t.me/calitronx")],
    ])
    welcomed = f"""
🎈Dear,
Sir,Ma'am  <b>{usrs}</b>

Use the below button or type /help for More info.
"""
    await message.reply_photo(
        "https://telegra.ph/file/ed28706fff93c4a2956e5.jpg",
        caption=welcomed,
        reply_markup=joinButton)
    raise StopPropagation
