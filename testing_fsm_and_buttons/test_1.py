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


@bot.message_handler(commands=["register"])
def register_start(message: types.Message, text: str = "Добро пожаловать!\n\nКем ты являешься?"):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Кто ты?"
    )
    keyboard.add(
        types.KeyboardButton("Участник"),
        types.KeyboardButton("Организтор"),
        row_width=2
    )
    msg = bot.send_message(
        chat_id=message.chat.id,
        text=text,
        reply_markup=keyboard
    )
    bot.register_next_step_handler(
        message=msg,
        callback=register_person_type,
        prev_msg_id=message.id
    )


def register_person_type(message: types.Message, prev_msg_id: int = None):
    if message.text not in ["Участник", "Организтор"]:
        register_start(message, "Выберите один из вариантов!")
        return

    if message.text == "Участник":
        msg = bot.send_message(
            chat_id=message.chat.id,
            text=f"Напиши мне свой возраст.\nprev_msg_id: {prev_msg_id}"
        )
        bot.register_next_step_handler(
            message=msg,
            callback=register_person_age
        )
    elif message.text == "Организтор":
        keyboard = types.InlineKeyboardMarkup(
            keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="Вывести список пользователей",
                        callback_data="registered_list"
                    ),
                    types.InlineKeyboardButton(
                        text="Выйти из меню",
                        callback_data="close_menu"
                    )
                ]
            ]
        )
        bot.send_message(
            chat_id=message.chat.id,
            text="Вот меню управления мероприятием",
            reply_markup=keyboard
        )
    else:
        pass


def register_person_age(message: types.Message):
    try:
        age = int(message.text)
    except ValueError:
        register_person_type(message)
        return

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Вы указали возраст {age}. Вы были добавлены в базу данных."
    )


@bot.callback_query_handler(func=lambda call: call.data == "registered_list")
def registered_list(call: types.CallbackQuery):
    bot.send_message(
        chat_id=call.message.chat.id,
        text="Список:\n\n\n\n\n\nempty"
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "close_menu")
def close_menu(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, text="Меню закрыто")
    bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.id
    )


@bot.message_handler(func=lambda m: True)
def echo_all(message: types.Message):
    bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
