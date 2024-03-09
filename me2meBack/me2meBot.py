import telebot
from telebot import types
import requests

bot = telebot.TeleBot('5481992398:AAEdg_t_MXgatnFYqnPYm2WLcjONo_uMPHc')


host = 'http://0.0.0.0:5000'


@bot.message_handler(content_types=['text'])
def confirm(message):
    markup = types.InlineKeyboardMarkup()
    btn_website = types.InlineKeyboardButton('Перейти на сайт', url='http://192.168.1.102:8000/')
    markup.add(btn_website)
    try:
        login = message.chat.username
        token = message.text.split()[1]
        requests.get(host + f'/confirm/{login}/{token}')
        bot.send_message(message.chat.id, 'Нажмите на кнопку, чтобы вернуться на сайт', reply_markup=markup)
    except:
        pass









bot.polling()
