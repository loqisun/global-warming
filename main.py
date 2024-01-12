key = 'your key'

import asyncio
import logging
import sys
import random

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from ai_bot import gpt

TOKEN = key

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, ЭКО друг! Я твой помощник в борьбе с глобальным потепление и готов предоставить любую помощь, которая тебе понадобится в этом! 
                         Вот, все то, что я могу сделать: [перечесление функций]")


@dp.message()
async def gpt(message: types.Message) -> None:

    try:
        if message.text == 'Как дела?':
            await message.answer('Нормально :)')
        else:
            await message.send_copy(chat_id=message.chat.id)
       

    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

link = 'https://docs.aiogram.dev/en/dev-3.x/#'