import telebot
from telebot import types
from random import choice
from datetime import datetime

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')
    bot.send_message(message.chat.id, 'я телеграм бот, чем вам помочь?!')
    with open('static/AnimatedSticker.tgs', 'rb') as stick:
        bot.send_sticker(message.chat.id, stick)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('Как ты')
    item2 = types.KeyboardButton('Что делаешь')
    item3 = types.KeyboardButton('Отправь стикер')
    item4 = types.KeyboardButton('Отправь время')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Выбери кнопку", reply_markup=markup)


@bot.message_handler(content_types=['text']) # обработка текста 
def text(message):
    if message.chat.type == 'private': # каждое сообщение должно быть защищенным, т.е. шифрованным, если оно шифрованное будем  отвечать
        if message.text == 'Как ты':
            bot.send_message(
                message.chat.id,
                'Отлично а у вас как?'
                )
        elif message.text == 'Что делаешь':
            bot.send_message(
                message.chat.id,
                'сижу думаю когда же вы меня улучшите'
            )
     
        elif message.text == 'Отправь время':
            time = datetime.today().strftime('%H:%M:%S')
            print(time)
            bot.send_message(message.chat.id,time+' 🕰')
        
        else:
            with open('static/AnimatedSticker.tgs', 'rb') as stick:
                bot.send_sticker(message.chat.id, stick)

bot.polling(non_stop=True)