import os

from telegram.ext.updater import Updater
#This will contain the API key we got from BotFather to specify in which bot we are adding functionalities to using our python code.
from telegram.update import Update
# This will invoke every time a bot receives an update i.e. message or command and will send the user a message.
from telegram.ext.callbackcontext import CallbackContext
#We will not use its functionality directly in our code but when we will be adding the dispatcher it is required (and it will work internally)
from telegram.ext.commandhandler import CommandHandler
#This Handler class is used to handle any command sent by the user to the bot, a command always starts with “/” i.e “/start”,”/help” etc.
from telegram.ext.messagehandler import MessageHandler
#This Handler class is used to handle any normal message sent by the user to the bot,
from telegram.ext.filters import Filters
#This will filter normal text, commands, images, etc from a sent message.


API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

updater = Updater(API_KEY, use_context=True)

def start(update : Update, callBack : CallbackContext):
    update.message.reply_text("Hello welcome how can i help you")

    

