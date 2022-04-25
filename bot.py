import telebot
import config
from translate import Translator

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types='text')
def translate(message):
    text = message.text
    languages = Translator(from_lang='ru', to_lang='en')
    translatedText = languages.translate(text)

    bot.send_message(message.chat.id, translatedText)
    
bot.polling(none_stop=True)