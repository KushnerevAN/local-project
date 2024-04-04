#import telebot
#from telebot import types

#bot = telebot.TeleBot('7169684743:AAFm_NcT1xF3ILx7KSFPagXLtAbjwqd_v9M')

#@bot.message_handler(commands=['start'])
#def start(message):
#    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
#    bot.send_message(message.chat.id, mess, parse_mode='html') # В () обращение к пользователю - сообщение - режим вывода

#@bot.message_handler(content_types=['text'])
#def get_user_text(message):
#    if message.text == 'Hello':
#        bot.send_message(message.chat.id, 'И тебе, привет!', parse_mode='html')
#    elif message.text == 'id':
#        bot.send_message(message.chat.id, f'Твой ID {message.from_user.id}', parse_mode='html')
#    elif message.text == 'photo':
#        photo = open('putin.jpeg', 'rb')
#        bot.send_photo(message.chat.id, photo, )

#@bot.message_handler(content_types=['photo'])
#def get_user_photo(message):
#    bot.send_message(message.chat.id, 'Вау, какое крутое фото')

#@bot.message_handler(commands=['website']) # Создание
#def website(message):
#    markup = types.InlineKeyboardMarkup() # данный класс позволяет создавать встроенные в сообщения "вещи"
#    markup.add(types.InlineKeyboardButton("Посетить вэб сайт", url="https://ya.ru")) # создание кнопки перехода на сайт
#    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

#@bot.message_handler(commands=['help']) # Создание
#def website(message):
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) # данный класс позволяет создавать кнопки снизу (Подстройка под рзмер экрана, кол-во кнопок в ряду)
#    website = types.KeyboardButton('Вэб-сайт') # Создание кнопки
#    start = types.KeyboardButton('Старт')
#    markup.add(website, start)

#bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

#bot.polling(none_stop=True) #Запуск бота, который работает постоянно