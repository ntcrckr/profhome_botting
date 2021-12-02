# importing pyTelegramBotAPI to use TeleBot class from within
import telebot

# importing config file where configuration constants are defined
import config

# initializing bot object
# parse_mode specifies a way for bot to parse strings sent to server
# None for as is, "HTML" or "MARKDOWN" for either
bot = telebot.TeleBot(config.token, parse_mode=None)


# decorator for send_welcome function
# the function will be called when specified command is called by user
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    # message object contains single message from user with all information that we could need
    # reply_to method sends a reply to the specified message with the given text
    bot.reply_to(message, "Хэй, как дела?")


# decorator for send_welcome function
# the function will be called for any message sent by user
@bot.message_handler(func=lambda m: True)  # lambda function returns True for every message
def echo_all(message):
    # message.text is a text of message sent by user
    bot.reply_to(message, message.text)


# main
if __name__ == "__main__":
    # infinite amount of update requests
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(e)
