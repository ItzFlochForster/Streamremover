#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "10811400")
API_HASH = os.environ.get("API_HASH", "191bf5ae7a6c39771e7b13cf4ffd1279")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8179604363:AAHUvF_Rs95t23XT057nfhh8ROVBXYHRhhQ")
CAPTION = os.environ.get("CAPTION", "")
DATABASE_URI = os.environ.get("DATABASE_URI", "naomi")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
ADMIN = int(os.environ.get("ADMIN", '6440021089'))
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://envs.sh/lHg.jpg"  # Replace with your Telegraph link
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002134572304)
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8081")) #8080


