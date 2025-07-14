from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext

from handlers.auth import register_user, get_categories, check_user
from handlers.product import cat_all_product_view


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    check=check_user(user.id,user.username)
    if not check:
        register_user(user.id, user.username)

    categories = get_categories()
    keyboard = [
        [InlineKeyboardButton(cat[1], callback_data=str(cat[0]))]
        for cat in categories
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Kategoriya tanlang:", reply_markup=reply_markup)
    # keyboard = [[cat[1]] for cat in categories]
    # reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    #
    # update.message.reply_text(
    #     f"Salom, {user.first_name}! Kategoriya tanlang:",
    #     reply_markup=reply_markup
    # )


def handle_category_callback(update, context):
    query = update.callback_query
    query.answer()  # callbackni tasdiqlash

    category_id = int(query.data)  # callback_data = '1', '2' ...

    products = cat_all_product_view(category_id)

    if products:
        response = "\n".join([f"{i + 1}. {p[1]}" for i, p in enumerate(products)])
    else:
        response = "Bu kategoriyada mahsulotlar yo'q."

    query.edit_message_text(text=response)

def order_

start_handler = CommandHandler("start", start)
