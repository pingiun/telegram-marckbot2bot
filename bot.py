from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update

import os
import re
import logging


def error_handler(update: Update, context: CallbackContext):
    logging.warning(f'Update {update} caused error {context.error}')


def substitute(update: Update, context: CallbackContext):
    try:
        match = context.matches[1]
        replace = context.matches[2]

        logging.info('match: %s - replace: %s', match, replace)

        substituted = re.sub(match, replace, update.message.reply_to_message.text)

        context.bot.sendMessage(update.message.chat.id, substituted)
    except AttributeError as e:
        logging.warning(e)


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater = Updater(token=os.environ['TG_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_error_handler(error_handler)

    # dispatcher.add_handler(CommandHandler('/assign', None))
    # dispatcher.add_handler(CommandHandler('/unassign', None))
    # dispatcher.add_handler(CommandHandler('/defines', None))
    dispatcher.add_handler(MessageHandler(Filters.regex(r's/(.+)/(.*)/'), substitute))
    # dispatcher.add_handler(MessageHandler(Filters.regex('/.+'), None))

    updater.start_polling()


if __name__ == '__main__':
    main()
