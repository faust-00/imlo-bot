from multiprocessing.managers import Token

from transliterate import to_latin, to_cyrillic

token = "7129814826:AAEDEyBlJ1iOv9r_w896i7-CPNiAeUMb024"
bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	javob = "Assalomu alaykum, xush kelibsiz."
	javob += "\nMatn kiriting:"
	bot.reply_to(message,  javob)

@bot.message_handler(func=lambda message: True)
def cyrillic_latin(message):
	msg = message.text
	javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
	bot.reply_to(message, javob(msg))

bot.polling()