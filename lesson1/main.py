import asyncio
import logging

import config
from aiogram import Bot, Dispatcher,types
from aiogram.filters.command import Command
import logging
import random

#create logging
logging.basicConfig(level=logging.INFO)

#create an object in bot
bot = Bot(token=config.token)

#dispatcher
dp = Dispatcher()

#/start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    print(message.chat)
    await message.answer(f'Привет, {name}')


async def main():
    await dp.start_polling(bot)

if __name__ =='__main__':
    asyncio.run(main())