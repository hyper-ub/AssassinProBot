import html
from telegram import Message, Update, Bot, User, Chat, ParseMode
from typing import List, Optional
from telegram.error import BadRequest, TelegramError
from telegram.ext import run_async, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import mention_html
from tg_bot import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, STRICT_GBAN, WHITELIST_USERS
from tg_bot.modules.helper_funcs.chat_status import user_admin, is_user_admin, sudo_plus
from tg_bot.modules.helper_funcs.extraction import extract_user, extract_user_and_text
from tg_bot.modules.helper_funcs.filters import CustomFilters
from tg_bot.modules.helper_funcs.misc import send_to_list
from tg_bot.modules.sql.users_sql import get_all_chats

GKICK_ERRORS = {
    "User is an administrator of the chat",
    "Chat not found",
    "Not enough rights to restrict/unrestrict chat member",
    "User_not_participant",
    "Peer_id_invalid",
    "Group chat was deactivated",
    "Need to be inviter of a user to kick it from a basic group",
    "Chat_admin_required",
    "Only the creator of a basic group can kick group administrators",
    "Channel_private",
    "Not in the chat",
    "Method is available for supergroup and channel chats only",
    "Reply message not found"
}

@run_async
@sudo_plus
def gkick(bot: Bot, update: Update, args: List[str]):
    log_msg = ""
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    user_id = extract_user(message, args)
    try:
        user_chat = bot.get_chat(user_id)
    except BadRequest as excp:
        if excp.message in GKICK_ERRORS:
            pass
        else:
            message.reply_text("User cannot be Globally kicked because: {}".format(excp.message))
            return
    except TelegramError:
            pass

    if not user_id:
        message.reply_text("You do not seems to be referring to a user")
        return
    if int(user_id) in SUDO_USERS or int(user_id) in SUPPORT_USERS:
        message.reply_text("OHHH! Someone's trying to gkick a sudo/support user! *Grabs Popcorn*")
        return
    if int(user_id) == OWNER_ID:
        message.reply_text("Wow! Someone's so noob that he want to gkick my owner! *Grabs Potato Chips*")
        return
    if int(user_id) == bot.id:
        message.reply_text("OHH... Let me kick myself.. No way... ")
        return
    if int(user_id) in WHITELIST_USERS:
        message.reply_text("OHHH! Someone's trying to gkick a whitelisted user! *Grabs Peanuts*")
        return
    chats = get_all_chats()

    start_time = time.time()
    datetime_fmt = "%H:%M - %d-%m-%Y"
    current_time = datetime.utcnow().strftime(datetime_fmt)
    if chat.type != 'private':
        chat_origin = "<b>{} ({})</b>\n".format(html.escape(chat.title), chat.id)
    else:
        chat_origin = "<b>{}</b>\n".format(chat.id)
    log_msg = (f"#GKICKED\n"
                f"<b>Originated from:</b> {chat_origin}\n"
                f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
                f"<b>Banned User:</b> {mention_html(user_chat.id, user_chat.first_name)}\n"
                f"<b>Banned User ID:</b> {user_chat.id}\n"
                f"<b>Event Stamp:</b> {current_time}")
    bot.send_message(MESSAGE_DUMP, log_msg, parse_mode=ParseMode.HTML)

    if user_chat.username:
        message.reply_text("Globally kicking user @{} ({})".format(user_chat.username, user_chat.user_id))
    else:
        message.reply_text("Globally kicking user with User ID {}".format(user_chat.user_id))

    for chat in chats:
        try:
             bot.unban_chat_member(chat.chat_id, user_id)  # Unban_member = kick (and not ban)
        except BadRequest as excp:
            if excp.message in GKICK_ERRORS:
                pass
            else:
                message.reply_text("User cannot be Globally kicked because: {}".format(excp.message))
                return
        except TelegramError:
            pass

GKICK_HANDLER = CommandHandler("gkick", gkick, pass_args=True)
dispatcher.add_handler(GKICK_HANDLER)

__mod_name__ = "Global Kick"
__handlers__ = [GKICK_HANDLER]
