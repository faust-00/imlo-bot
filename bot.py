import logging
from aiogram import Bot, Dispatcher, executor, types
from checkWord import check_words
from transliterate import to_cyrillic, to_latin
API_TOKEN = '7508673269:AAEYGu0nPX0pmom_cY4KLjME1148AZ9CuTw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Assalomu alaykum, Imlo botga xush kelibsiz!")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Botga biror so'z yuboring.")


@dp.message_handler()
async def send_check_words(message: types.Message):
    msg_text = message.text.split()
    for word in msg_text:
        cyrillic = lambda msg: to_cyrillic(msg) if msg.isascii() else msg
        result = check_words(cyrillic(word))

        if result['available']:
            response = f"✅{word.capitalize()}"
        else:
            response = f"❌ {word.capitalize()}\n"
            original_form = lambda msg, original_word: to_latin(msg) if original_word.isascii() else msg

            for text in result['matches']:
                response += f"✅{original_form(text, word).capitalize()}\n"

        await message.answer(response)


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)