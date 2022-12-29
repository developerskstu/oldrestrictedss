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
SESSION = "AQCBZe5iy4s27VSiwBTjPC07jh5obPXxYugTYTl50WXtImtDgwFNyH0C0DuaSAHwsaF3wnkikA11z-lUdluiBLhjri_w4fuzFS9w52TOZOPAlBoaPZcy6paUUo2OnXEkUWzN0T-01OsR0-YbwZl9lO0sY2lZR-7VyZ_LQLXRvleyEJ8kGzag2VzAqYc_P_0huvJXZu1DA9Ez1mtzFQLrEvG-IlM9RW_0joKFEehZIkZqSQLz4LiaOdMsrDoCTnXBEvksWg0PJlXfb4neDtLezfHGr0bweVudt3_O1I-u4o9P5r81olER9yDxPUlw6FlEnMhxO4eXNIiRYJRgLjGBwhv8AAAAAUk7U9cA"
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
