import telebot
import config
from googletrans import Translator

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Русский🇷🇺')
    btn2 = telebot.types.KeyboardButton('Английский🇬🇧')
    btn3 = telebot.types.KeyboardButton('Арабский🇸🇦')
    btn4 = telebot.types.KeyboardButton('Итальянский🇮🇹')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text='Привет, {0.first_name}!\nВыбери язык, на который нужен перевод текста: '.format(message.from_user), reply_markup=markup)

def func(message, lang):
    def trans(message):
        translator = Translator()
        translateText = translator.translate(message.text, dest=lang)
        bot.send_message(message.chat.id, text=translateText.text)
    msg = bot.send_message(message.chat.id, text='Введите текст:')
    bot.register_next_step_handler(msg, trans)


@bot.message_handler(content_types='text')
def translate(message):
    try:
        if(message.text == 'Русский🇷🇺'):
            func(message, 'ru')
        elif(message.text == 'Английский🇬🇧'):
            func(message, 'en')
        elif(message.text == 'Арабский🇸🇦'):
            func(message, 'ar')
        elif(message.text == 'Итальянский🇮🇹'):
            func(message, 'it')
    except Exception:
        bot.send_message(message.chat.id, text='Упс... Произошла ошибка!')

bot.polling(none_stop=True)
