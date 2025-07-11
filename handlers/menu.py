from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext

def menu(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Tugma 1", callback_data='1')],
        [InlineKeyboardButton("Tugma 2", callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Quyidagi tugmalardan birini tanlang:", reply_markup=reply_markup)

def button_handler_func(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(f"Siz {query.data}-tugmani tanladingiz.")

menu_handler = CommandHandler("menu", menu)
button_handler = CallbackQueryHandler(button_handler_func)
