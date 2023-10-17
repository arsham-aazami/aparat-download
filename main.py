import os

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

updater = Updater(API_KEY, use_context=True)

