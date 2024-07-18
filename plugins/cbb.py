#Coded by @Its_Tartaglia_Childe

from pyrogram import Client 
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = f"<b>Bot Cammands\n❏ Commands For BOT Admins\n├/start : start the bot or get posts\n├/batch : create link for more than one posts\n├/genlink : create link for one post\n├/users : view bot statistics\n├/broadcast : broadcast any messages to bot users\n└/stats : checking your bot uptime\n\n👨‍💻 Developed by <a href=https://t.me/straw_hat_bots>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ ꭙ 𝐁ᴏᴛs</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ​", callback_data="close"),
                        InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text = f"<b>Owner - @Virtual_Monster </a>\nMy Channel - <a href=https://t.me/jjustanime>HindiSub Anime</a>\nSupport Group - <a href=https://t.me/Request4anime>Support</a>\n\n👨‍💻 Developed by <a href=https://t.me/Straw_Hat_Bots>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ ꭙ 𝐁ᴏᴛs</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("​ᴄʟᴏꜱᴇ​", callback_data="close"),
                        InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
