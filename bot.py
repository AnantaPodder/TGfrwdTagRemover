from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import Config
from telegram import ParseMode
from cmd import startCMD, helpCMD
from func import *

updater = Updater(Config.TOKEN)
disPatch = updater.dispatcher


disPatch.add_handler(CommandHandler('start', startCMD))
disPatch.add_handler(CommandHandler('help', helpCMD))


disPatch.add_handler(MessageHandler(Filters.text, Captionfunc))
disPatch.add_handler(MessageHandler(Filters.document, Filefunc))
disPatch.add_handler(MessageHandler(Filters.video, Mediafunc))
disPatch.add_handler(MessageHandler(Filters.photo, Photofunc))
disPatch.add_handler(MessageHandler(Filters.sticker, Stickerfunc))
disPatch.add_handler(MessageHandler(Filters.voice, Voicefunc))
disPatch.add_handler(MessageHandler(Filters.audio, Audiofunc))


updater.start_polling()
updater.idle()
