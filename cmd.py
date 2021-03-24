from config import Config
from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup


buttonGroup = [[InlineKeyboardButton('AshuCyber', url=Config.Channel)], [
    InlineKeyboardButton('Ping me', url="https://t.me/anantapodder")]]

buttonKeyboard = InlineKeyboardMarkup(buttonGroup)


def startCMD(update, context):
    try:
        update.message.reply_text(Config.welcome_Message.format(
            update.message.from_user.full_name), reply_markup=buttonKeyboard, parse_mode=ParseMode.HTML)
    except Exception as e:
        update.message.reply_text(e)


def helpCMD(update, context):
    try:
        update.message.reply_text(
            Config.help_text, reply_markup=buttonKeyboard, parse_mode=ParseMode.HTML)
    except Exception as e:
        update.message.reply_text(e)
