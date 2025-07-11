from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
from geopy.geocoders import Nominatim

def location_request(update: Update, context: CallbackContext):
    button = KeyboardButton("Joylashuvimni yuborish", request_location=True)
    markup = ReplyKeyboardMarkup([[button]], resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text("Joylashuvingizni yuboring:", reply_markup=markup)

def handle_location(update: Update, context: CallbackContext):
    location = update.message.location
    lat, lon = location.latitude, location.longitude

    geolocator = Nominatim(user_agent="my_location_bot")
    address = geolocator.reverse((lat, lon), language='ru')

    update.message.reply_text(f"Siz joylashgan manzil:\n{address.address}")

location_handler = CommandHandler("location", location_request)
location_receiver_handler = MessageHandler(Filters.location, handle_location)
