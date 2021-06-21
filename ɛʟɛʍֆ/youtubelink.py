from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["link"]), group=-2)
async def love(_, message):
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍕𝗘𝗗𝗠🍕", url="https://t.me/")],
        [InlineKeyboardButton("🍤𝗟𝗼-𝗙𝗶🍤:", url="https://t.me/")],
        [InlineKeyboardButton("🍨𝗧𝗥𝗔𝗣.𝗕𝗘𝗔𝗧🍨:", url="https://t.me/")],
        [InlineKeyboardButton("🌭𝗡𝗖𝗦🌭:", url="https://t.me/")],
        [InlineKeyboardButton("🍪𝗣𝗢𝗣🍪:", url="https://t.me/")]
    ])
    youtube_ex = f"""
**Some example youtube channels and songs if you don't know what u want**📺
- type /love if i helped u anyway🍗🍔🍟🍕
```ƈǟʟɨȶʀօռӼ``` """
    await message.reply_photo(
        "https://telegra.ph/file/ed28706fff93c4a2956e5.jpg",
        reply_markup=joinButton,
        caption=youtube_ex
        )
    raise StopPropagation