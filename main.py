from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
import os
import random
import time
from io import BytesIO, FileIO
bot = Bot(token='1570067009:AAHjsnuf80BUesvJWSIQ3qSGa0aTIK4rw3w')
disp = Dispatcher(bot)


ferrets_count = 1

@disp.message_handler(commands=['start', 'help'])
async def helping(message: types.Message):
    await message.answer("""Чтобы получить хорька отправь слово хорек
    Можешь загрузить своего хорька, отправив фото. Оно станет доступно всем""")

@disp.message_handler(content_types=ContentType.PHOTO)
async def add_ferret(message: types.Message):
    ferret_name = f'ferret_{message.chat.id}_{int(time.time())}.jpg'
    await message.photo[-1].download(destination='./ferrets/' + ferret_name)


@disp.message_handler(regexp=r'.*хор[е, ё, ь]к.*')
async def ferret(message: types.Message):
    global ferrets_count
    ferret_image = open('./ferrets/' + random.choice(os.listdir('./ferrets')), 'rb')
    text = f'хорьков: {ferrets_count}'
    ferrets_count += 1

    await bot.send_photo(message.chat.id, ferret_image)
    await message.answer(text)


if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True)