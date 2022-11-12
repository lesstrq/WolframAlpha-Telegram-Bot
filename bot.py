import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_API_TOKEN, PROXY_URL
from wolfram_integration import get_link

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_help(message: types.Message):
    await message.answer("Hello there!\nUse the /query command to get some knowledge from WolframAlpha\ni.e.: /query x^2 - 5x + 6 = 0")

@dp.message_handler(commands=['query'])
async def send_wolfram_image(message: types.Message):
    query = message.text[7:]
    await message.answer_photo(get_link(query))

@dp.message_handler()
async def send_unknown(message: types.Message):
    await message.answer("I am not sure what exactly do you want from me...\nUse the /help or the /start command so we can understand each other!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

