import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message: types.Message):
    bot.send_message(message.from_user.id, "Хэй, как дела?")


@bot.message_handler(commands=["help"])
def send_help(message: types.Message):
    bot.send_message(message.from_user.id, "Я бот!")


@bot.message_handler(commands=["reply_buttons"])
def reply_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        # selective=None,
        # row_width=3,
        input_field_placeholder="Choose..."
    )
    keyboard.add(
        types.KeyboardButton("Yes"),
        types.KeyboardButton("No"),
        row_width=2
    )
    bot.send_message(
        chat_id=message.chat.id,
        text="Choose one",
        reply_markup=keyboard
    )


@bot.message_handler(commands=["inline_buttons"])
def inline_buttons(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Button 1",
                    callback_data="b1"
                ),
                types.InlineKeyboardButton(
                    text="Button 2",
                    callback_data="b2"
                )
            ]
        ]
    )
    bot.send_message(
        chat_id=message.chat.id,
        text="Tap one button",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_all(call: types.CallbackQuery):
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.id
    )
    bot.send_message(
        chat_id=call.message.chat.id,
        text=call.data
    )
    bot.answer_callback_query(call.id, text="Template text")


@bot.message_handler(func=lambda m: True)
def echo_all(message: types.Message):
    bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
