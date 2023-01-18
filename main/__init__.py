#Github.com/8769Anurag

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24229815
API_HASH = "6d03e392b1200580a85ef243f83a48a5"
BOT_TOKEN = "5818737155:AAFgEZ3p6PGaHmKqW3QcLEotCb_EsDba9xg"
SESSION = "AQBrKY_UCC6VPNfqbq3_0-22vzbMlt8GruFkTuEgDdFVtwW42z7TpFanIooeoLfqT9MUEPr4MRWIvpfRDQJRbXGxeuxm0szlX4N99ERn0DAjyBLsrjKngsAOgtzyo2QiY2KRYagGQHiLwUacAcve4Aksi49haczFB2Gc9cxIyYSgtTzCKaiwinlevyls5nfki7556sg5dZDwzvAa-pNsYYtWlNNL0oEEhbDr534yPLRZYHdJed0lbWiKFo-AhdBw4IFwQRkJLpu9oNGNlBfI87PYIkn6EzDQeZbK5dQrXTn9i7hnel2r2HDunS0q16P0sKM_tFC8tZlgEnt9a0eS5xLXAAAAAUk7U9cA"
FORCESUB = "tested_botss"
AUTH = 5523592151

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
