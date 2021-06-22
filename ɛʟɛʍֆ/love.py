from pyrogram import Client, filters, StopPropagation
from pyrogram.types import Message
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )
from Trial import *

@Client.on_message(
    filters.command("love", prefixes='/')
                   ) 
async def love(
    _,
    ydl: Message
    ):
  usrs = ydl.from_user.first_name
  joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("💋LOVE:", url="https://t.me/tronxli")],
    ])
  Aww = f"""Hey <b>{ydl.from_user.first_name}</b>
🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟

If you liked my project and want to be a GitHub contributor then:
- 📧You may email me at **calitronvrtx@gmail.com**
- 📬You can personal message me in Telegram **@calitronx**   
- ✨Star & Fork my GitHub repo.\n

If you liked my project and want and just want to make me happy then you can:
- 🌹share my bot and make me happy 🌹
    
**<b>{usrs}**</b> Thanks a lot for using my bot🍰

🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟
"""      
  await ydl.reply_photo(
        youliurl,
        reply_markup=joinButton,
        caption=Aww
        )
  raise StopPropagation