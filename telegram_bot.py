import os
import logging

from dotenv import load_dotenv
from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters
)

from handlers import hello_user, download_docs

load_dotenv()

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(os.getenv('TELEGRAM_TOKEN'), use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', hello_user))
    dp.add_handler(MessageHandler(Filters.document, download_docs))

    logging.info("Start bot")
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
