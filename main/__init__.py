#Github.com/8769Anurag

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 18105029
API_HASH = "f3143f24c70415ca357cc9fd27a1d72f"
BOT_TOKEN = "5841270397:AAHm9zCnp58lAipCEXMQIttOvTg7-siKfaM"
SESSION = "AQBIkCKyPUdMxoL_6Z8I4LurXsUBVECxc9f4fpjOGnVC95gwY7enrWd8i35eRII7Gia_1-W3di8YN8p0bVwmSWq6wAxIaagNgQvwBlygbMCDB03kpQhF4szN1VYE3be0PAgBNug1vQvDWzgdw7NBlMMbTkxtTT4gx2o8UfGlFLpzVlBFqqD2dxUyb8eZ7VvD1XLRJB747WYEgCi8kD0M0tVPBfmzasQCyWuVFG-T6WL5GNwGizMtMz7FOfAz1kGWnKJG03VKa-IM913DKHRdecY4Yw-WyghnKKjrtANu5W0q02Oq23-kNXAAv5JqDXrDKP8HLqshj9iGVzb3PoztxuNnAAAAATWA_dAA"
FORCESUB = "testedd_botss"
AUTH = 5192613328

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
