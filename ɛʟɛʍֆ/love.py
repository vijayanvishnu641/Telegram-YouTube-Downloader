from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["love"]), group=-2)
async def love(_, message):
  usrs = message.from_user.first_name
  joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("💋LOVE:", url="https://t.me/tronxli")],
    ])
  Aww = f"""Hey <b>{message.from_user.first_name}</b>
If you liked my project and want to be a GitHub contributor then:
- 📧You may email me at **calitronvrtx@gmail.com**
- 📬You can personal message me in Telegram **@calitronx**   
- ✨Star & Fork my GitHub repo.\n

If you liked my project and want and just want to make me happy then you can:
- 🌹share my bot and make me happy 🌹
    
**<b>{usrs}**</b> Thanks a lot for using my bot🍰
"""      
  await message.reply_photo(
        "https://telegra.ph/file/ed28706fff93c4a2956e5.jpg",
        reply_markup=joinButton,
        caption=Aww
        )
  raise StopPropagation