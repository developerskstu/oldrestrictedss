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
SESSION = "AQBB46UJ9ndmiBnWqLDr-MgfKzdoYsiZg75_O2jeppWL2uhGipcMNYn59hpb7BSRhX4XurZdHd9F-Z8LkNUF_FPKM_ajUFo3m2b5KImZWQ_h10aK_Wo3SLRgZ8OZDZprQLmlDrr8gt5oZxkE8OPvSIWw461mtM2PoZhlv6FOKfBIsbZYZPx_ipf6Smw9h0dUzHHOi6pbrZ_bB3wr44yzg7UV-RkDpgbEegdhpsC_Eln3IouX5CabrE_9ErU8gW4fR08Ge0IIRvMtHNadFuqtmGlair2oicAGN296k7l7nTyHFLKPsyq3dbN660XpviFZxLfmh3Ps3n1bxLmwF4o9TvwIAAAAATWA_dAA"
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
