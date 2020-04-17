import json
import os

def get_user_list(config, key):
    with open('{}/tg_bot/{}'.format(os.getcwd(), config), 'r') as json_file:
        return json.load(json_file)[key]

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.class Config(object):
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "750944856:AAHc-0wVffY0LKDGJydOkr6IQ4so6bZ19aA"
    OWNER_ID = "716243352"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Skuzzy_xD"
    SUPPORT_GROUP = "DraXRoBotsSupport"
    SUPPORT_CHANNEL = "DraXRoBots"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://dxcucqwe:zN3ate2ltVBqClVXG3M2M17SoxdlFYA8@motty.db.elephantsql.com:5432/dxcucqwe'  # needed for any database modules
    MESSAGE_DUMP = -1001451926178  # needed to make sure 'save from' messages persist
    GBAN_LOGS = MESSAGE_DUMP
    LOAD = []
    NO_LOAD = ['connection', 'bluetext_cleaner', 'feds', 'dev', 'reactions', 'shout', 'speedtest', 'dbcleanup']
    WEBHOOK = False
    URL = None
    MAPS_API = ""
    API_OPENWEATHER = ""
    AI_API_KEY = "2b9f51208687db80b87856204843f498a6e61843bfd32cb99cb68e08850d35eabd0723da"
    WALL_API = "e7b346f40f069a7fb0df3a8aaf6bac2c"

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = get_user_list('elevated_users.json', 'sudos')  # List of id's -  (not usernames) for users which have sudo access to the bot.
    DEV_USERS = get_user_list('elevated_users.json', 'devs')  # List of id's - (not usernames) for developers who will have the same perms as the owner
    SUPPORT_USERS = get_user_list('elevated_users.json', 'supports')  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    #WHITELIST_USERS = get_user_list('elevated_users.json', 'whitelists')  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_USERS = SUDO_USERS + DEV_USERS + SUPPORT_USERS
    SPAMMERS = []
    DONATION_LINK = ""  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = "CAACAgUAAx0CVoqiogACEjdebzRcse2hFYYuxUrbmM8G2IJYxAACpAADrPaBV414-el7wFHIGAQ"  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /
    CASH_API_KEY = "ZKRIQPI9PEBC847A" # Get one from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = "PGMJQHM4QRFX" # Get one from https://timezonedb.com/register
    HEROKU_API_KEY = "6e1388d2-f432-483f-8af1-a9a77a384987"
    HEROKU_APP_NAME = "agent47bot"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
