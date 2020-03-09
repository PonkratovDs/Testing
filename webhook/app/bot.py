import telebot

bot = telebot.TeleBot('1137407455:AAGxUDa2uiYaDlljJ8_6Vztk98JLrY7DA54')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()