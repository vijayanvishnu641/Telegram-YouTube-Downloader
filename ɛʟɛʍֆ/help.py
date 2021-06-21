from pyrogram import Client, filters
from Trial import *

@Client.on_message(filters.command(["help"]))
async def help(_, message):
    helptxt = f"""
.📍**𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓**📍.
-**♥ Bigger download size,more wait time ♥**
-𝐅𝐢𝐥𝐞 𝐬𝐢𝐳𝐞 𝐦𝐨𝐫𝐞 𝐭𝐡𝐞𝐧 𝟐𝐠𝐛 𝐰𝐨𝐧'𝐭 𝐛𝐞 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐝𝐮𝐞 𝐭𝐨 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐩𝐨𝐥𝐢𝐜𝐲."""
        
    await message.reply_photo(
        "https://telegra.ph/file/ed28706fff93c4a2956e5.jpg",
        caption=helptxt
        )