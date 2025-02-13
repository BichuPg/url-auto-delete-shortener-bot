import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Popcorn')
API_ID = int(environ.get('API_ID', '12192489'))
API_HASH = environ.get('API_HASH', 'ed39e721f5d4fd6d3c05121c1661b8ea')
BOT_TOKEN = environ.get('BOT_TOKEN', '5748537217:AAEzSD90oQu992zEtqDI-w8dXg8km9Q4ce8')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/5eaf79965acbe524cb892.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5097048997').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001850600075').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5097048997').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', 'mongodb+srv://moviescheckpoints:1@cluster0.rd7llap.mongodb.net/?retryWrites=true&w=majority')
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Popcorn')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001867240136'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Technical_Bots_Chat')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "ɴᴀᴍᴇ: <code>{file_name}</code> \n\nJᴏɪɴ Nᴏᴡ: [⚡Technical Bots⚡](https://t.me/Technical _Bots)</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b><i>📟 ᴛɪᴛᴛʟᴇ :</b></i> {title} \n<b><i>🌟 ʀᴀᴛɪɴɢ :</b></i> {rating} \n<b><i>🎭 ɢᴇɴʀᴇ :</b></i> {genres} \n<b><i>📆 ʀᴇʟᴇᴀsᴇ :</b></i> {year} </b></i>\n<b><i>⏰ ᴅᴜʀᴀᴛɪᴏɴ :</b></i> {runtime}\n\n<b><i>🔖 𝓟𝓵𝓸𝓽  :</b></i> `{plot}` \n\n<b><i>⚡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ⚡ :</b></i> {message.chat.title}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001938477678')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

    
# URL Shortener 

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'ziplinker.net')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '5b343a256452228dae2eb40201f9e8a64583357f') # useless don't fill 

# Auto Delete For Group Message (Self Delete) 
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 3600))
SELF_DELETE = environ.get('SELF_DELETE', False)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/+AKANipq4DHhkYjk9"

   # Custom Caption Under Button #
CAPTION_BUTTON = "✅ Updates Channel"
CAPTION_BUTTON_URL = "https://t.me/Technical_Bots"

   # Auto Delete For Bot Sending Files 
