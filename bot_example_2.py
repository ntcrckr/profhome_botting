import telebot
import config
from telebot import types

# file where all functions are declared
import utility

bot = telebot.TeleBot(config.token, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message: types.Message):
    utility.send_welcome(bot, message)


@bot.message_handler(commands=["help"])
def send_help(message: types.Message):
    utility.send_help(bot, message)


@bot.message_handler(commands=["time"])
def send_time(message: types.Message):
    utility.send_time(bot, message)


@bot.message_handler(regexp="Здравствуй*")
def kind_answer(message: types.Message):
    utility.kind_answer(bot, message)


@bot.message_handler(func=utility.check_forwarded)
def forwarded_answer(message: types.Message):
    utility.forwarded_answer(bot, message)


@bot.message_handler(content_types=["photo"])
def photo_answer(message: types.Message):
    utility.photo_answer(bot, message)


@bot.message_handler(chat_types=["group"])
def group_answer(message: types.Message):
    utility.group_answer(bot, message)


@bot.message_handler(func=lambda m: True)
def echo_all(message: types.Message):
    utility.echo_all(bot, message)


if __name__ == "__main__":
    bot.infinity_polling()
