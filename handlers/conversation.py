from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

STEP1, STEP2 = range(2)

def start_conv(update: Update, context: CallbackContext):
    update.message.reply_text("Ismingizni kiriting:")
    return STEP1

def step1(update: Update, context: CallbackContext):
    context.user_data["ism"] = update.message.text
    update.message.reply_text("Familiyangizni kiriting:")
    return STEP2

def step2(update: Update, context: CallbackContext):
    context.user_data["familiya"] = update.message.text
    update.message.reply_text(f"Rahmat, {context.user_data['ism']} {context.user_data['familiya']}!")
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Bekor qilindi.")
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("anketa", start_conv)],
    states={
        STEP1: [MessageHandler(Filters.text & ~Filters.command, step1)],
        STEP2: [MessageHandler(Filters.text & ~Filters.command, step2)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
