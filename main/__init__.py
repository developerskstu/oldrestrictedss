#Github.com/8769Anurag

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 25733211
API_HASH = "e0d2f6d53490d4a6ce5fecce2dd8e25b"
BOT_TOKEN = "6068536413:AAHGo7Y_17NSLXN54NfxwkR3gJ_4ahTuVtg"
SESSION = "AQCpKcQZeDtiezPUack9pnx8sHJCEQqm1vC6x9ZbyJ2tohRGz4qnXayvt0j06XvIoitYet50lVgdZrdRO-86nFzs2YJUkcIto0xD30CUYMOXh8EdPG2VotOLGDpIsHsfEmL1zvk1bePaYVuA7UQAoBwE-HPDNzY2g0tg6TpKXp4R_1oqAZNoTm_7eDtOzM_zUqeX4l-lMBd6Pzfs-x9AJPfw6H53zX07fUKh5W4VMbfw9fY4grk7xa6Xekg0VtJCBfgNrI65hJjr71Yal6D7QhWPyc-dVTYzSrrwfHPQTnTg_sQtgIwHWuIRlGDpg2_Yu_sBnhNqg4AzFrwdOj8UugrqAAAAAUxAXxEA"
FORCESUB = "ttest_botsss"
AUTH = 5574254353

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
