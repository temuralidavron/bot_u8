from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def info(update: Update, context: CallbackContext):
    user = update.message.from_user
    msg = f"Ism: {user.first_name}\n"
    msg += f"Familiya: {user.last_name or '-'}\n"
    msg += f"Username: @{user.username or '-'}\n"
    msg += f"Telegram ID: {user.id}"
    update.message.reply_text(msg)

info_handler = CommandHandler("info", info)
