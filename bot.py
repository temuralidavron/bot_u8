from telegram.ext import Updater

from handlers.location import location_handler, location_receiver_handler
from handlers.start import start_handler
# from handlers.echo import echo_handler
from handlers.info import info_handler
from handlers.menu import menu_handler, button_handler
from handlers.conversation import conv_handler

def main():
    updater = Updater("7877779975:AAFmt98Hvhbxmu6d0xe0psaht9_Q-Fy1qBs", use_context=True)
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(start_handler)
    # dp.add_handler(echo_handler)
    dp.add_handler(info_handler)
    dp.add_handler(menu_handler)
    dp.add_handler(button_handler)
    dp.add_handler(conv_handler)
    dp.add_handler(location_handler)
    dp.add_handler(location_receiver_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
