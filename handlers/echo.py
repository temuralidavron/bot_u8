# from telegram import Update
# from telegram.ext import MessageHandler, Filters, CallbackContext
#
# def echo(update: Update, context: CallbackContext):
#     user_text = update.message.text
#     update.message.reply_text(f"Siz yozdingiz: {user_text}")
#
# echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)
