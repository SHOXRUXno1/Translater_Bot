from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from googletrans import Translator
from loader import dp

tarjima=Translator()
@dp.message_handler(Command("translater"))
async def bot_trans(message: types.Message):
    matn = message.text
    tarjimon = tarjima.translate(matn,dest='en')
    tarjima_qilindi = tarjimon.text
    await message.reply(tarjima_qilindi)
if name == 'main':
    executor.start_polling(dp, skip_updates=True)
