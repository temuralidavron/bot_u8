from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext

from handlers.auth import register_user, get_categories, check_user


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    check=check_user(user.id,user.username)
    if not check:
        register_user(user.id, user.username)

    categories = get_categories()
    keyboard = [[cat[1]] for cat in categories]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text(
        f"Salom, {user.first_name}! Kategoriya tanlang:",
        reply_markup=reply_markup
    )





start_handler = CommandHandler("start", start)
