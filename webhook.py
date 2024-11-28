from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('token')

bot = TeleBot(TOKEN)

bot.remove_webhook()
bot.set_webhook('https://stagning.koratvplus.com/')