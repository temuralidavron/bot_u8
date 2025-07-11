from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom! Men sizning Telegram botingizman.")

start_handler = CommandHandler("start", start)
