from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from datetime import datetime
import logging

TOKEN = 'YOUR_TELEGRAM_TOKEN'

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Will be called everytime /start command is received
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='So, you have cravings for movie?')

# The real chat method which will reply acccordingly
def chat(bot, update):
    # TODO implement get_reply
    # reply = get_reply(update.message.text)
    reply = 'I have received: {}'.format(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=reply)

# A command method to capitalize the message
def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(update.message.chat_id, text=text_caps)

# A command method to return current datetime
def date(bot, update):
    curr_time = datetime.now().strftime('%B %d, %Y %H:%M')
    bot.send_message(update.message.chat_id, text=curr_time)

# Unknown command handler
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

chat_handler = MessageHandler(Filters.text, chat)
dispatcher.add_handler(chat_handler)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

date_handler = CommandHandler('date', date)
dispatcher.add_handler(date_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
