import telebot
import config
from googletrans import Translator

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Русский🇷🇺')
    btn2 = telebot.types.KeyboardButton('Английский🇬🇧')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Привет, {0.first_name}!\nВыбери язык, на который нужен перевод текста: '.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types='text')
def translate(message):
    if(message.text == 'Русский🇷🇺'):
        def trans(message):
            translator = Translator()
            translateText = translator.translate(message.text, dest='ru')
            bot.send_message(message.chat.id, text=translateText.text)
            msg = bot.send_message(message.chat.id, text='Введите текст:')
            bot.register_next_step_handler(msg, trans)
        msg = bot.send_message(message.chat.id, text='Введите текст:')
        bot.register_next_step_handler(msg, trans)
    elif(message.text =='Английский🇬🇧'):
        def trans(message):
            translator = Translator()
            translateText = translator.translate(message.text, dest='en')
            bot.send_message(message.chat.id, text=translateText.text)
            msg = bot.send_message(message.chat.id, text='Введите текст:')
            bot.register_next_step_handler(msg, trans)
        msg = bot.send_message(message.chat.id, text='Введите текст:')
        bot.register_next_step_handler(msg, trans)

bot.polling(none_stop=True)
