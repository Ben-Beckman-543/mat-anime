#(©)CodeXBotz
#Recoded By @Its_Tartaglia_Childe



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7161487035:AAFJQRQrj-SetCK1Fixy44kazxKZ2RDOo9s")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28525384"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3a1190585fe5bf1f6324be87ba5b68c6")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-100210960095"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6911235730"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://nico_music_bot:ahmed3434@cluster01.rnm5fc4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster01")
DB_NAME = os.environ.get("DATABASE_NAME", "MAT_Anime")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002100237972"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002170138276"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Kᴏɴɴɪᴄʜɪᴡᴀ!! {mention} ⚡,\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Mikey_anime_team'>𝐌𝐀𝐓 𝐀ɴɪᴍᴇ</a></b>")
try:
    ADMINS=[6727550037]
    for x in (os.environ.get("ADMINS", " 7162615398 6727550037 5355745915 5834350988 5747882115").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}🔥,\n\nApko File tabhi milegi jab Aap in dono channels ko join karke notification on kar loge, Ye kaam karte he Aap link Per dubara Click kro File Mil jayegi\n\nThank you 🙏")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Mikey_anime_team"

ADMINS.append(OWNER_ID)
ADMINS.append(6727550037)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
