import requests
from aiogram import Bot, Dispatcher, executor, types


TOKEN = '6251868136:AAHDVKgMGBjtg7lgzmOfKqo6fMqjYXVu3wM'
OPENWEATHERTOKEN ='01df24ba06738fcc92ce5212727ce42a'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_function(message: types.Message):
    await message.reply("Hello")


@dp.message_handler()
async def echo(massage: types.Message):
    await massage.answer(massage.text)


if __name__ == '__main__':
    executor.start_polling(dp)


# import requests
# from aiogram import Bot, Dispatcher, executor, types
#
#
# TOKEN = '6091118625:AAEhQxESYwVk2aQDE5nMYxtyR0Yh0gRBnNk'
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start'])
# async def start_function(message: types.Message):
#     await message.reply("add sneakers name")
#
# @dp.message_handler()
# async def echo(massage: types.Message):
#     await massage.answer(massage.text)
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
