import os


class Config:
    TOKEN = os.environ.get("BOT_TOKEN", None)

    welcome_Message = "Hi {}, \n<b>Welcome to Telegram Forward Tag remover Bot</b>\n Use Command /help to know more about the bot."
    help_text = "You can remove 'forwared from .....' text from any message or media you send. \n\n <b> forward me anything and I will do magic.</b>"
    Channel = "https://t.me/ashucyber"
