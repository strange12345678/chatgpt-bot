# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , " ")
API_HASH = environ.get("API_HASH" , " ")
BOT_TOKEN = environ.get("BOT_TOKEN" , " ")
ADMIN = int(environ.get("ADMIN" , "7861690278"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", " "))
LOG_CHANNEL = environ.get("LOG_CHANNEL", " ")
MONGO_URL = environ.get("MONGO_URL" , " ")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", " ")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
