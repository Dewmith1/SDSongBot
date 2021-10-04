#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
👋𝐇𝐞𝐲 [{}](tg://user?id={}), 𝐈'𝐦 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐒𝐨𝐧𝐠 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭 🎵

🎧 Just send me the song name you want to download.🎧
      eg:```/song Pretty savage blackpink🇰🇷```
      
🎶𝐀 𝐛𝐨𝐭 𝐛𝐲 @IMkashyapaa🎶
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="𝔻𝕖𝕧🌷", url="https://t.me/IMkashyapaa"
                    ),
                    InlineKeyboardButton(
                        text="🎙𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩🎙️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ SDSongBot is online.")
idle()
