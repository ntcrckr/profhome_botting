import telebot
import config

# file with definitions for every object inside pyTelegramBotAPI library
# importing to clearly define function parameters
from telebot import types

# time library for casting int to string
import time

bot = telebot.TeleBot(config.token, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message: types.Message):
    bot.send_message(message.from_user.id, "Хэй, как дела?")


@bot.message_handler(commands=["help"])
def send_help(message: types.Message):
    bot.send_message(message.from_user.id, "Я бот!")


@bot.message_handler(commands=["time"])
def send_time(message: types.Message):
    bot.send_message(message.from_user.id, time.ctime(message.date))


@bot.message_handler(regexp="Здравствуй*")
def kind_answer(message: types.Message):
    bot.send_message(message.from_user.id, "Ты так вежлив!")


def check_forwarded(message: types.Message):
    if message.forward_from is None:
        return False
    else:
        return True


@bot.message_handler(func=check_forwarded)
def forwarded_answer(message: types.Message):
    bot.send_message(message.from_user.id, "О, ты что-то переслал!")


@bot.message_handler(content_types=["photo"])
def photo_answer(message: types.Message):
    bot.send_message(message.from_user.id, "Классное фото!")


@bot.message_handler(chat_types=["group"])
def photo_answer(message: types.Message):
    bot.send_message(message.chat.id, "Всем привет!")


@bot.message_handler(func=lambda m: True)
def echo_all(message: types.Message):
    bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
