import telebot
from telebot import types

import time


def send_welcome(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, "Хэй, как дела?")


def send_help(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, "Я бот!")


def send_time(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, time.ctime(message.date))


def kind_answer(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, "Ты так вежлив!")


def check_forwarded(message: types.Message):
    if message.forward_from is None:
        return False
    else:
        return True


def forwarded_answer(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, "О, ты что-то переслал!")


def photo_answer(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, "Классное фото!")


def group_answer(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.chat.id, "Всем привет!")


def echo_all(bot: telebot.TeleBot, message: types.Message):
    bot.send_message(message.from_user.id, message.text)
