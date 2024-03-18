import telebot

bot = telebot.TeleBot('7169684743:AAFm_NcT1xF3ILx7KSFPagXLtAbjwqd_v9M')

@bot.message_handler(comands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


bot.polling(none_stop=True) #Запуск бота, который работает постоянно