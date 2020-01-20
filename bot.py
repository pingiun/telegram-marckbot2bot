from telegram.ext import Updater, Dispatcher, CommandHandler, RegexHandler

import os


def main():
    updater = Updater(token=os.environ['TG_TOKEN'])
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('/assign', lambda: None))
    dispatcher.add_handler(CommandHandler('/unassign', lambda: None))
    dispatcher.add_handler(CommandHandler('/defines', lambda: None))
    dispatcher.add_handler(RegexHandler('s/.+/.*/', lambda: None))
    dispatcher.add_handler(RegexHandler('/.+', lambda: None))

    updater.start_polling()


if __name__ == '__main__':
    main()