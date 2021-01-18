# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 2340yoo
API_HASH = "927cadiooyd8eb4790ab141c54a29"

# Get this from @Botfather
TOKEN = "156oyoAH0-pmy0NsbFTchnO7cj3OXopl2umLDvk0"

# Your mongodb uri
MONGO_DB_URI = ""

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    
]

# The ID of the group where your bot streams
GROUP = -
# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Send "now playing" messages to the group
LOG = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 5

# No need to touch the following.
LOG_GROUP = GROUP if LOG else None
SUDO_FILTER = filters.user(SUDO_USERS)
