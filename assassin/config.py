class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1125785992:AAGJdlLPPBB27kUzdEquB5kqZ7LFahaL1EU"
    OWNER_ID = "1031840046"
    OWNER_USERNAME = "Amazers_xD"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://itydknou:TItgiEgHW_2b8IUCLGuc1Lu0tK4dyC0x@rajje.db.elephantsql.com:5432/itydknou'
    MESSAGE_DUMP = -489941031
    SUPPORT_GROUP = "AssassinRoBotSupport"
    SUPPORT_CHANNEL = "AssassinUpdates"
    LOAD = []
    NO_LOAD = ['translation', 'sed']
    WEBHOOK = False
    URL = None
    AI_API_KEY = "739c4d1e5c1369da40c27588dcf4b3f77f886a0c133440721030cb7e0ae4ab5f51ce8be66659bd0fbac5d5d64d655d56231d03f1087a4df3004ae6e0ba7d614f"
    
    # OPTIONAL
    SUDO_USERS = [919262859,761486644,636314540]
    DEV_USERS = [716243352]
    SUPPORT_USERS = [989553010,680915808,665812580]
    WHITELIST_USERS = [636314540]
    SPAMMERS = [696570394]
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_ANTISPAM = True
    WORKERS = 8
    BAN_STICKER = 'CAACAgUAAxkBAAIBk15p4qi7J0TU1PmYN7sePwpfP8TcAAKLAQACnTktN77so16zcvIJGAQ'
    STRICT_GBAN = True
    STRICT_GMUTE = True
    GBAN_LOGS = MESSAGE_DUMP
    ALLOW_EXCL = True
    API_OPENWEATHER = '7b19e0a0c79a5e6024a0d2b2838c8d88'
    
    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True